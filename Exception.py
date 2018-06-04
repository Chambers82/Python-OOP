# Programmer: Brent Chambers
# Date: 06/03/2018
# filename: Exception.py
# Summary: Inheriting the Exception Class
# Description: MyError inherits from the Exception class, and contains a custom str function that is called when the exception is raised. 
# Requirements: 


class MyError(Exception):
	# *args accepts any number of arguments
	# pass any args, all objects will be stored in args
	# can all pass no arguments
	def __init__(self, *args):
		print 'calling init'
		if args:
			self.message = args[0]
		else:
			self.message = None
			
	# Gets called when exception is raised
	def __str__(self):
		print 'calling str'
		if self.message:
			return "here's a mMyError exception: {0}".format(self.message)
		else:
			return "here's an exception"
			
# Raise Exception without argument
#raise MyError


# Raise Exception with an argument
raise MyError("Greetings good Fellow")