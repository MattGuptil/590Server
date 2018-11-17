import numpy as np
from user_class import User
from flask import Flask, jsonify, request
import datetime

myUsers = [] ;


@app.route("/heart_rate/average/<name>", methods = ["GET"])
def get_avgHR(name):
	""" This GET function grabs the AvgHR for a user.

	Returns:
		A dictionary of the AvgHR in JSON dictionary form.

	"""
	myName = "{}".format(name)
	myResults = dataRetreiver(myName, "AvgHR")

	return myResults

@app.route("heart_rate/<name>", methods = ["GET"])
def get_heartrate(name):
	""" This GET function grabs the heart rate data of the user entered.

	Returns:
		Heart rate data of user in JSON dictionary form.


	"""
	myName = "{}".format(name)
	myResults = dataRetreiver(myName, "HR")

	return myResults


@app.route("/heart_rate", methods=["POST"])
def heart_rate():
	""" This is the POST function that allows a user to enter information.

	Returns:
		Nothing, simply stors the data given by user.		


	"""
	r = request.get_json()
	email = r['user_email']
	HR = r['heart_rate']
	age = r['user_age']
	time = datetime.datetime.now()

	newUser = checkNewU(email)
	if not newUser[0]:
		myU = create_NewUser(email, HR, age, 60, time)
	else:
		myU = addto_User(newUser[1], HR, age, time)

	myU = calcAv(myU)
	myUsers.append(myU)
	return

def create_NewUser(myE, myHR, myA, myAvg, myTi):
	""" This function creates a new User object with associated input values.

	Args:
		myE: String Email address of user.
		myHR: float64, heart rate of user.
		myA: int, age of user.
		myAvg: int, forced average heart rate.
		myTi: string, time at point of data entry.

	Returns:
		A User object with associated input values installed.


	"""
	x = User(myE, myHR, myA, myAvg, myTi)
	return x

## add code for average later
def addto_User(myUse, myHR, myA, myTi):
	""" This function takes in a User object and changes age, and appends time/HR.

	Args:
		myUse: User object that will be modified.
		myA: Int Age of user that will be added.
		myHR: Float HR of user that will be appended to numpy array.
		myTi: String of time that will be appended to time list.

	Returns:
		Modified User object.


	"""
	myUse.change_age(myA)
	myUse.add_HR(myHR)
	myUse.add_time(myTi)
	return myUse


def checkNewU(us_email):
	""" This function takes the users email and checks to see if they exist in memory.

	Args:
		us_email: String, of Users email

	Returns:
		True and the object of given user if found, and False if user was not found.


	"""
	for key in myUsers:
		if key.email() == us_email:
			return [True, key]
	return [False, 0]


def calcAv(thisUser):
	""" This function calls the average property function of the User Object.

	Args:
		thisUser: User Object of current user that will be modified.

	Returns:
		The User Object with an updated AvgHR property.


	"""
	thisUser.calc_AvgHR()
	return thisUser


def dataRetreiver(name, prop):
	""" This function will take in user email and output desired results based on call location.

	Args:
		name: String, This is the users email address in String form
		prop: String, This is the property of the User object that is being requested.

	Returns:
		Jsonified dictionary if user was found, along with proper exit code.

	Raises:
		ValueError: If the email name entered does not match a current user, will return proper exit code.

	"""
	myResults = checkNewU(name)

	if not myResults[0]:
		raise ValueError("Error: User does not exist, please submit User data and try again.")
		return False, 440

	myObj = myResults[1]
	if prop == "AvgHR":
		myData = myObj.AvgHR
	if prop == "HR":
		myData = myObj.HR
	if prop == "age":
		myData = myObj.age
	
	myDir = {"Heart Rates": myData} ## probable have to add {}".format(myData)

	return jsonify(myDir), 200



if __name__ == '__main__':
	app.run(host="0.0.0.0")