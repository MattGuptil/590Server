import numpy as np
from user_class import User
from flask import Flask, jsonify, request
import datetime
import requests
import json
from server_methods import *
app = Flask(__name__)

myUsers = [] ;


@app.route("/status/<name>", methods = ["GET"])
def get_status(name):
	""" This GET function grabs the AvgHR for a user.

	Returns:
		A dictionary of the AvgHR in JSON dictionary form.

	"""
	myName = "{}".format(name)
	myResults = dataRetreiver(myName, "status") ## Need to jsonify dictionary

	return myResults


@app.route("/heart_rate/average/<name>", methods = ["GET"])
def get_avgHR(name):
	""" This GET function grabs the AvgHR for a user.

	Returns:
		A dictionary of the AvgHR in JSON dictionary form.

	"""
	myName = "{}".format(name)
	myResults = dataRetreiver(myName, "AvgHR") ## Need to jsonify dictionary

	return myResults

@app.route("/heart_rate/<name>", methods = ["GET"])
def get_heartrate(name):
	""" This GET function grabs the heart rate data of the user entered.

	Returns:
		Heart rate data of user in JSON dictionary form.


	"""
	myName = "{}".format(name)
	myResults = dataRetreiver(myName, "HR") ## jsonify dictionary ## see note on line 122 of server_methods

	return myResults


@app.route("/new_patient", methods=["POST"])
def new_patient():
	""" This is the POST function that allows a user to create/enter information.

	Returns:
		Nothing, simply stors the data given by user.		


	"""
	r = request.get_json()

	### add code to validate entries.
	email = r['attending_email']
	#HR = r['heart_rate']
	age = r['user_age']
	age = int(age)
	#time = datetime.datetime.now() ### gotta make this into a string....
	#time = time.strftime("%Y-%m-%d %I:%M:%S.%f")
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
		Nothing, just posts HR data to user while checking to make sure default values are removed.		


	"""
	r = request.get_json()

	myid = r['patient_id']
	myhr = r['hear_rate']
	myhr = int(myhr)
	time = datetime.datetime.now() ### gotta make this into a string....
	time = time.strftime("%Y-%m-%d %I:%M:%S.%f")

	newUser = checkNewU(myid)
	myU = newUser[1]
	if not newUser[0]:
		raise ValueError("User does not yet exist try another patient id or create a new user.")
	else:
		myU = addto_User(myU, myHR, [myTi])
		del myUsers[newUser[2]]
		myUsers.append(myU)


	isTac = isTachy(myhr, myU.age)
	#if isTac:
		###send an email

	return


@app.route("/heart_rate/interval_average", methods=["POST"])
def interval_average():
	""" This is the POST function that allows a user to get HR average over interval.

	Returns:
		Dictionary jsonified, of the average heart rate over an interval.		


	"""
	r = request.get_json()

	myid = r['patient_id']
	trange = r['heart_rate_average_since']

	newt = datetime.datetime.strptime(trange, "%Y-%m-%d %I:%M:%S.%f")
	mydict = timeSorter(myid,newt)

	return jsonify(mydict), 200



if __name__ == '__main__':
	app.run(host="127.0.0.1")