# Programmer: Brent E. Chambers
# Date: 06/03/2018
# Filename: PropertyAttribs.py
# Summary: Encapsulation and the Setting of Attributes
# Description: @property is a decorator that designates an instance attribute as 
# encapsulable through methods
# @property is not about control, but convienence
# Lets the user of our class use simple attribute access

class GetSet(object):
	def __init__(self, value):
		self.attrval = value
		
	@property
	def var(self):
		print 'getting the "var" attribute'
		return.self.attrval
		
	@var.setter
	def var(self, value):
		print 'setting the "var" attribute'
		self.attrval = value
		
	@var.deleter
	def var(self):
		print 'deleting the "var" attribute'
		self.attrval = None
		
me = GetSet(5)
me.var = 1000
print me.var
del me.var
print me.var

# @property should not encapsulate expensive operations, because 
# attribute setting looks cheap

# @property controls attributes that are expected, but can't c
# control attributes that are unexpected

# __slots__ can define allowable attributes
# saves memory by defining attributes ahead of time
# shouldn't be used to limit attributes
