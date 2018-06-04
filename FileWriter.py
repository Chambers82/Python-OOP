# Programmer: Brent E. Chambers
# Date: 06/03/2018
# Filename: FileWriter.py
# Description: A collection of class objects for writing content to a file
#    each class inheriets from object, and declares additional functions for the object

from datetime import datetime

class WriteFile(object):
	def __init__(self, filename, writer):
		self.fh = open(filename, 'w')
		self.formatter = writer()
		
	def write(self, text):
		self.fh.write(self.formatter.format(text))
		self.fh.write('\n')
	
	def close(self):
		self.fh.close()
		

class CVSFormatter(object):
	def __init__(self):
		self.delim = ','
		
	def format(self, this_list):
		new_list = []
		for element in this_list:
			if self.delim in element:
				new_list.append('"{0}"'.format(element))
			else:
				new_list.append(element)
		return self.delim.join(new_list)

class LogFormatter(object):
	def format(self, this_line):
		dt = datetime.now()
		date_str = dt.strftime('%Y-%m-%d %H:%M')
		return "{0}		{1}".format(date_str, this_line)