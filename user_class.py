import numpy as np


class User(object):


	#The "self" has to be first parameter
	def __init__(self, email_arg, age_arg = 0, HR_arg = np.array([]), 
		AvgHR_arg = 0.0, time_arg = []):

		# two underscores __ will hide it
		self.email = email_arg
		self.HR = HR_arg
		self.age = age_arg
		self.AvgHR = AvgHR_arg
		self.time = time_arg


	def change_age(self,new_age):
		""" This function allows an age to be changed or added.

		Args:
			self: This is the object that will call the function.
			new_eage: This will be the string that marks the new user age.

		Returns:
			Nothing, only changes.	


		"""

		if not isinstance(new_age, int) or new_age is None:
			raise TypeError("Error: Age Entered was not an integer. Please Input a correct age.")
		self.age = new_age


	def add_HR(self,new_HR):
		""" This function allows a Heart Rate to be added to the Numpy array of HR.

		Args:
			self: This is the object that will call the function.
			new_HR: Float or Integer that will be appended.

		Returns:
			Nothing, only changes.	


		"""
		if not isinstance(new_HR, int) or new_HR is None:
			raise TypeError("Error: HR entered was not an integer.")
		self.HR = np.append(self.HR, new_HR) 


	def change_AvgHR(self,new_AvgHR):
		""" This function allows an AvgHR to be changed or added.

		Args:
			self: This is the object that will call the function.
			new_AvgHR: This will be a float that shows Average heart rate.

		Returns:
			Nothing, only changes.	


		"""
		if not isinstance(new_AvgHR, int) or new_AvgHR is None:
			raise TypeError("Error: AvgHR entered was not an integer.")
		self.AvgHR = new_AvgHR 

 
	def add_time(self,new_time):
		""" This function allows a time to be added to the list of times.

		Args:
			self: This is the object that will call the function.
			new_time: String that gets added to list

		Returns:
			Nothing, only changes.	


		"""
		if not isinstance(new_time, str) or new_time is None:
			raise TypeError("Error: Time entered was not a string.")
		myT = self.time
		self.time = myT.append(new_time) 


	def calc_AvgHR(self):
		""" This function will calculate and return the average heart rate.

		Args:
			self: The object that heart rate data will be taken from.

		Returns:
			Nothing, just changes the average heart rate value which is a float64

		"""
		myData = self.HR
		myAv = np.mean(myData)
		self.AvgHR = myAv