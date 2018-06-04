# Programmer: Brent E. Chambers
# Date: 06/03/2018
# Filename: FileWrite.py
# Description: A class object heirarchy for writing content to a file

import datetime
class WriteFile(object):
	def __init__(self, filename):
		self.writer = open(filename, 'w')
	def write(self, txt):
		write_text = txt
		self.writer.write(write_text)
class LogFile(WriteFile):
	def write(self, txt):
		dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
		self.writer.write(dt_str + "  " + txt + "\n")
class DelimFile(WriteFile):
	def __init__(self, filename, delim=","):
		self.delim = delim
		self.writer = open(filename, 'w')
	def write(self, values):
		self.writer.write(self.delim.join(values)+"\n")
		
"""
log = LogFile('log.txt') 
mydelim = DelimFile('data.csv', ',')
log.write('this is a log message')
log.write('this is another log message')
mydelim.write(['a', 'b', 'c', 'd'])
mydelim.write(['1', '2', '3', '4']) 
"""
	