import numpy as np
from user_class import User
from flask import Flask, jsonify, request
import datetime
import requests
import json
import server


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

    if not isinstance(hr, np.int32) and not isinstance(hr,
                                                       int) or not isinstance(
            age, int):
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
