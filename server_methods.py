import numpy as np
from user_class import User
from flask import Flask, jsonify, request
import datetime
import requests
import json

def create_NewUser(myE, myHR, myA, myAvg, myTi):
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
	if not isinstance(myE, str) or not isinstance(myA, int) or not isinstance(myTi, list) or not isinstance(myAvg, float):
		raise TypeError("Error: Values did not match correct types. Please try again.")
	myHR = np.array([myHR])
	x = User(myE, myA, myHR, myAvg, myTi)
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
	if not isinstance(myUse, User) or not isinstance(myHR, int) or not isinstance(myA, int) or not isinstance(myTi, str):
		raise TypeError("Error: Values did not match correct types. Please try again.")
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
	if not isinstance(us_email, str) or us_email is None:
		raise TypeError("Error: Value entered was not a String. Can not be compared.")
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
	if not isinstance(thisUser, User) or thisUser is None:
		raise TypeError("Error: The type of variable entered was not a User Object.")
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
	elif prop == "HR":
		myData = myObj.HR
	elif prop == "age":
		myData = myObj.age
	else:
		raise ValueError("Fatal: A valid object property was not called. Debugging Needed.")
	
	myDir = {"Heart Rates": myData} ## probable have to add {}".format(myData)

	return jsonify(myDir), 200