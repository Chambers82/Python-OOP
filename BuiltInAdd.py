# Programmer: Brent E. Chambers
# Date: 06/03/2018
# Filename: BuiltInAdd.py
# Description: This demontration shows the builtin functions of objects that are used
#  in pythonic operations and expressions e.g. "String1 + String2"
# Syntactical Magic Methods
#
# __add__ is a built in function that python sees as a plus sign '+'
# __repr__ 

class SumList(object):
	def __init__(self, this_list):
		self.mylist = this_list

	#Broadcasting:
	#adding each element of a list and creating a list with each sum
	def __add__(self, other):
		new_list = [x+y for x,y in zip(self.mylist, other.mylist)]
		return SumList(new_list)
	
	# does the same as above:
	# new_list = []
	# zipped_list = zip(self.mylist, other.mylist)
	# for tup in zipped_list:
	# 	new_list.append(tup[0] + tup[1])

	#called implicily when the object is printed
	def __repr__(self):
		return str(self.mylist)
		

# This demonstrates the ease at which python code is developed and read.  This power
# is the ability to show what the object is about.
"""
'abc' in var 		var.__contains__('abc')
var == 'abc'		var.__eq__('abc')
var[1]				var.__getitem__(1)
var[1:3]			var.__getslice__(1, 3)
len(var)			var.__len__()
print var			var.__repr__()
"""
