import numpy as np
from user_class import User
from flask import Flask, jsonify, request
import datetime
import requests
import json
import sendgrid
import os
from sendgrid.helpers.mail import *

# from server_methods import *
app = Flask(__name__)

myUsers = []
Allowed_keys = [

    "patient_id",
    "attending_email",
    "heart_rate",
    "heart_rate_average_since",
    "user_age"

]


@app.route("/status/<name>", methods=["GET"])
def get_status(name):
    """ This GET function grabs the AvgHR for a user.

    Returns:
        A dictionary of the AvgHR in JSON dictionary form.

    """
    myName = "{}".format(name)
    myResults = dataRetreiver(myName, "status")

    return jsonify(myResults), 200


@app.route("/heart_rate/average/<name>", methods=["GET"])
def get_avgHR(name):
    """ This GET function grabs the AvgHR for a user.

    Returns:
        A dictionary of the AvgHR in JSON dictionary form.

    """
    myName = "{}".format(name)
    myResults = dataRetreiver(myName, "AvgHR")

    return jsonify(myResults), 200


@app.route("/heart_rate/<name>", methods=["GET"])
def get_heartrate(name):
    """ This GET function grabs the heart rate data of the user entered.

    Returns:
        Heart rate data of user in JSON dictionary form.


    """
    myName = "{}".format(name)
    # print("AHHHHHHHHHHHHHHHH", myUsers[0].id)
    myResults = dataRetreiver(myName,
                              "HR")
    # print("AHHHHHHHHHHHHHHHH", myResults)
    return jsonify(myResults), 200


@app.route("/new_patient", methods=["POST"])
def new_patient():
    """ This is the POST function that allows a user to create/enter information.

    Returns:
        Nothing, simply stors the data given by user.


    """
    r = request.get_json()
    try:
        validate_request(r)
    except TypeError:
        return jsonify({"message": 'wrong format'}), 500

    email = r['attending_email']
    # HR = r['heart_rate']
    age = r['user_age']
    age = int(age)
    # time = datetime.datetime.now() ### gotta make this into a string....
    # time = time.strftime("%Y-%m-%d %I:%M:%S.%f")
    myID = r['patient_id']

    newUser = checkNewU(myID)
    if not newUser[0]:
        myU = create_NewUser(email, 0, age, 60.0, [' '], myID)
    else:
        raise ValueError("patient_id exists please use a different patient_id")

    myUsers.append(myU)
    return jsonify({'Num users': len(myUsers), 'Newuse': 's'}), 200


@app.route("/heart_rate", methods=["POST"])
def heart_rate():
    """ This is the POST function that allows a user to Post HR data.

    Returns:
        Nothing, just posts HR data to user while checking to make sure default
         values are removed.


    """
    r = request.get_json()
    try:
        validate_request(r)
    except TypeError:
        return jsonify({"message": 'wrong format'}), 500

    myid = r['patient_id']
    myhr = r['heart_rate']
    myhr = int(myhr)
    time = datetime.datetime.now()
    time = time.strftime("%Y-%m-%d %I:%M:%S.%f")

    newUser = checkNewU(myid)
    myU = newUser[1]
    if not newUser[0]:
        raise ValueError(
            "User does not yet exist try another patient id or create a new "
            "user.")
    else:
        myU = addto_User(myU, myhr, [time])
        del myUsers[newUser[2]]
        myUsers.append(myU)

    isTac = isTachy(myhr, myU.age)
    if isTac:
        emailTac(myU.email)

    return jsonify({'Num users': len(myUsers), 'Newuse': isTac}), 200


@app.route("/heart_rate/interval_average", methods=["POST"])
def interval_average():
    """ This is the POST function that allows a user to get HR average over
        interval.

    Returns:
        Dictionary jsonified, of the average heart rate over an interval.


    """
    r = request.get_json()
    try:
        validate_request(r)
    except TypeError:
        return jsonify({"message": 'wrong format'}), 500
    myid = r['patient_id']
    trange = r['heart_rate_average_since']

    newt = datetime.datetime.strptime(trange, "%Y-%m-%d %I:%M:%S.%f")
    mydict = timeSorter(myid, newt)

    return jsonify(mydict), 200


def emailTac(myem):
    """ This function will email the attending physician and warn of Tachy.

    Args:
        myem: string of email for attending physician.

    Returns:
        Nothing, just sends out the email.


    """
    from stringkey import sg as sg

    from_email = Email("test@example.com")
    to_email = Email(myem)
    subject = "Patient going Tachy!"
    content = Content("text/plain",
                      "Alert: Please attend to patient, they are showing signs"
                      " of Tachy")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

    return


def validate_request(req):
    """ This function was leveraged from Suyash Kumar and his server.py script
        with class files.

    Args:
        req: request object with headers

    Returns:
        Nothing

    Raises:
        ValidationError: If key is not within acceptable keys then this returns
            a bad value.


    """
    req = req.keys()

    for key in req:
        if key not in Allowed_keys:
            raise TypeError("Key '{0}' not present in request".format(key))


def create_NewUser(myE, myHR, myA, myAvg, myTi, myID):
    """ This function creates a new User object with associated input values.

    Args:
        myE: String Email address of user.
        myHR: float64, heart rate of user. Converts to np.array
        myA: int, age of user.
        myAvg: int, forced average heart rate.
        myTi: string, time at point of data entry.

    Returns:
        A User object with associated input values installed.


    """
    if not isinstance(myE, str) or not isinstance(myA, int) or not isinstance(
            myTi, list) or not isinstance(myAvg, float):
        raise TypeError(
            "Error: Values did not match correct types. Please try again.")
    if not isinstance(myHR, int) and not isinstance(myHR, float):
        raise TypeError(
            "Error2: Values did not match correct types. Please try again.")
    myHR = np.array([myHR])
    x = User(myE, myA, myHR, myAvg, myTi, myID)
    return x


def addto_User(myUse, myHR, myTi):
    """ This function takes in a User object and changes age, and appends
        time/HR.

    Args:
        myUse: User object that will be modified.
        myHR: Float HR of user that will be appended to numpy array.
        myTi: String of time that will be appended to time list.

    Returns:
        Modified User object.


    """
    if not isinstance(myUse, User) or not isinstance(myHR,
                                                     int) or not isinstance(
            myTi, list):
        raise TypeError(
            "Error: Values did not match correct types. Please try again.")
    myUse.add_HR(myHR)
    myUse.add_time(myTi)

    myArray = myUse.HR
    if myArray[0] == 0:
        myArray = np.delete(myArray, 0)
    myUse.HR = myArray
    myUse = calcAv(myUse)
    if myUse.time[0] == ' ':
        del myUse.time[0]

    return myUse


def checkNewU(us_ID):
    """ This function takes the users id and checks to see if they exist in
        memory.

    Args:
        us_email: String, of Users id

    Returns:
        True and the object of given user if found, and False if user was not
            found.


    """
    if not isinstance(us_ID, str) or us_ID is None:
        raise TypeError(
            "Error: Value entered was not a String. Can not be compared.")
    i = 0
    for key in myUsers:
        if key.id == us_ID:
            return [True, key, i]
        i = i + 1
    return [False, myUsers]


def calcAv(thisUser):
    """ This function calls the average property function of the User Object.

    Args:
        thisUser: User Object of current user that will be modified.

    Returns:
        The User Object with an updated AvgHR property.


    """
    if not isinstance(thisUser, User) or thisUser is None:
        raise TypeError(
            "Error: The type of variable entered was not a User Object.")
    thisUser.calc_AvgHR()
    return thisUser


def dataRetreiver(name, prop):
    """ This function will take in user email and output desired results based
        on call location.

    Args:
        name: String, This is the users email address in String form
        prop: String, This is the property of the User object that is being
            requested.

    Returns:
        Jsonified dictionary if user was found, along with proper exit code.

    Raises:
        ValueError: If the email name entered does not match a current user,
            will return proper exit code.

    """
    myResults = checkNewU(name)

    if not myResults[0]:
        raise ValueError(
            "Error: User does not exist, please submit User data and try "
            "again.")

    myObj = myResults[1]
    if prop == "AvgHR":
        myData = myObj.AvgHR
        myDir = {
            "Avg Heart Rate": myData}
    elif prop == "HR":
        myData = myObj.HR
        myData = myData.tolist()
        myDir = {
            "Heart Rates": myData}
    elif prop == "status":
        myl = len(myObj.HR) - 1
        myData = myObj.HR[myl]
        myage = myObj.age
        myData = isTachy(myData, myage)
        myDir = {"isTachy": myData, "Time": myObj.time[
            myl]}
    else:
        raise ValueError(
            "Fatal: A valid object property was not called. Debugging Needed.")

    return myDir


def timeSorter(myid, newt):
    """ This function grab the patient id and time given and then finds the
        average over the interval.

    Args:
        myid: String, that reps patient id.
        newt: String, represents the time that the user entered to find average
            time after this has occured.

    Returns:
        Dictionary containing avg value.

    Raises:
        ValueError: If the user does not exist.


    """
    holder = checkNewU(myid)
    if not holder[0]:
        raise ValueError(
            "Error: User does not currently exist, please first enter user"
            " data then attempt this.")
    i = 0
    j = 0
    for each in holder[1].time:
        myt = datetime.datetime.strptime(each, "%Y-%m-%d %I:%M:%S.%f")
        if i == len(holder[1].time) - 1:
            j = -1
            break
        if newt <= myt:
            j = i
            break
        i = i + 1

    if j == -1:
        return {"Bad Date": 'Try Again'}

    k = 0
    z = 0
    avgholder = 0.0
    for each in holder[1].HR:
        if k >= j:
            avgholder = avgholder + each
            z = z + 1
        k = k + 1
    avgholder = avgholder / float(z)

    mydict = {'Avg Heart Rate over your Interval': avgholder}

    return mydict


def isTachy(hr, age):
    """ This function checks to see if the patient is tachycardic based on age
        and resting hr.

    Args:
        hr: int or numpyfloat, that reps last heart rate taken.
        age: int, age of patient.

    Returns:
        True or False based on whether or not patient is tachy.


    """

    if not isinstance(
            hr,
            np.int32) and not isinstance(
            hr,
            int) and not isinstance(
                hr,
                np.int64) or not isinstance(
                    age,
            int):
        raise TypeError("Error: hr or age was not correct type.", type(hr))

    if hr > 151 and age >= 1 and age <= 2:
        return True
    elif hr > 137 and age >= 3 and age <= 4:
        return True
    elif hr > 133 and age >= 5 and age <= 7:
        return True
    elif hr > 130 and age >= 8 and age <= 11:
        return True
    elif hr > 119 and age >= 12 and age <= 15:
        return True
    elif hr > 100 and age >= 15:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(host="127.0.0.1")
