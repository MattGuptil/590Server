import numpy as np
from user_class import User
from flask import Flask, jsonify, request
import datetime

myUsers = [] ;

@app.route("/hear_rate", methods=["POST"])
def heart_rate():
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


	myUsers.append(myU)
	return

def create_NewUser(myE, myHR, myA, myAvg, myTi):
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
	for key in myUsers:
		if key.email() == us_email:
			return [True, key]
	return [False, 0]


def myAv(thisUser):
	


if __name__ == '__main__':
	app.run(host="0.0.0.0")