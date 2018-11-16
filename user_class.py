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


	def output_fullname(self):
		fullName = self.lastname + " " + self.lastname


	def change_email(self,new_email):
		self.__email = new_email


	def add_HR(self,new_HR):
		self.__HR = np.append(self.HR, new_HR) 


	def change_AvgHR(self,new_AvgHR):
		self.__AvgHR = new_AvgHR 


	def add_time(self,new_time):
		myT = self.time
		self.__HR = myT.append(new_time) 






	@property
	def w(self):
		return self._weight

	# or @w.setter
	def set_weight(self,input):
		self.__weight = input