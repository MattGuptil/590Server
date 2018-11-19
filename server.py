import numpy as np
from user_class import User
from flask import Flask, jsonify, request
import datetime
import requests
import json

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

	### add code to validate entries.
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

if __name__ == '__main__':
	app.run(host="0.0.0.0")