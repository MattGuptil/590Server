import numpy as np
from user_class import User
from flask import Flask, jsonify, request
import datetime
import requests
import json
app = Flask(__name__)

myUsers = [] ;


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
	time = datetime.datetime.now() ### gotta make this into a string....
	time = time.strftime("%Y-%m-%d %I:%M:%S.%f")

	newUser = checkNewU(email)
	if not newUser[0]:
		myU = create_NewUser(email, HR, age, 60, time)
	else:
		myU = addto_User(newUser[1], HR, age, time)

	myU = calcAv(myU)
	myUsers.append(myU)
	return

@app.route("/heart_rate/interval_average", methods=["POST"])
def interval_average():
	""" This is the POST function that allows a user to get HR average over interval.

	Returns:
		Dictionary jsonified, of the average heart rate over an interval.		


	"""
	r = request.get_json()

	email = r['user_email']
	trange = r['hear_rate_average_since']

	newt = datetime.strptime(trange, "%Y-%m-%d %I:%M:%S.%f")


	holder = checkNewU(email)
	if not holder[0]:
		raise ValueError("Error: User does not currently exist, please first enter user data then attempt this.")
	i = 0
	j = 0
	for each in holder[1].time:
		myt = datetime.strptime(each, "%Y-%m-%d %I:%M:%S.%f")
		if i == len(holder[1].time)-1:
			j = -1
			break
		if newt <= myt :
			j = i
			break
		i= i+1

	if j == -1:
		return {"Bad Date": 'Try Again'}

	k = 0
	avgholder = 0.0
	for each in holder[1].HR:
		if k >= j:
			avgholder = avgholder + each
		k = k + 1
	avgholder = avgholder/float(len(avgholder))

	mydict = {'Avg Heart Rate over your Interval': avgholder}

	return mydict ## look at other code to jsonify


if __name__ == '__main__':
	app.run(host="0.0.0.0")