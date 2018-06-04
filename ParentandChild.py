# Programmer: Brent E. Chambers
# Date: 06/03/2018
# Filename: ParentandChild.py
# Summary: Inheritance Example with Parent and Sub-classes (408)
# Description:  The following example illustrates inheritance with a parent class (GetSetParent, who 
#    extends Object) to sub-class GetSetInt (who overloads showdoc), and GetSetList.

import abc

class GetSetParent(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self, value):
		self.val = 0
	def set_val(self, value):
		self.val = value
	def get_val(self):
		return self.val
	@abc.abstractmethod
	def showdoc(self):
		return
		
		
class GetSetInt(GetSetParent):
	# Redefine set_val so its value is checked and is an integer
	def set_val(self, value):
		if not isinstance(value, int):
			value = 0
		# "Specializing" making use of the behavior in both
		# Look for super class of GetSetInt (GetParent) and pass value as an argument
		super(GetSetInt, self).set_val(value)
	# Show doc is required of all classes that inherit from GetSetParent
	def showdoc(self):
		# Inserting values into a string.  Getting the ID of the instance (self)
		print('GetSetInt object ({0}), only accepts integer values'.format(id(self)))


class GetSetList(GetSetParent):
	
	def __init__(self, value=0):
		self.vallist = [value]

	#Overwrites the parent class with getting the last element
	def get_val(self):
		return self.vallist[-1]

	def get_vals(self):
		return self.vallist
		
	def set_val(self, value):
		self.vallist.append(value)
	
	def showdoc(self):
		print('GetSetList object, len{0}, stores history of values set'.format(len(self.vallist)))
		