# Programmer: Brent Chambers
# Date: 06/03/2018
# filename: ConfigFileToDict.py
# Summary: Leveraging a dictionary to stand behind a Configuration File
# Description: ConfigDict object inherits from obj dict, and upon inititialization, will read a file
#   containing key,value pairs, and convert the content into a dictionary.  
# Requirements:
'''
A file of key,value pairs

Our config file should looks like this:

sql_query=SELECT this FROM that WHERE condition
email_to=me@mydomain.com
num_retries=5

In order to implement a dictionary, ConfigDict will 
inherit from dict (the dictionary class), so in most respects it will act like a dictionary.  

'''
import string

class ConfigDict(dict):
	_config = ''
	def __init__(self, config_file):
		self._config = config_file
		if os.path.isfile(self._config):
			with open(self.config) as fh:
				for line in fh:
					key, val = line.split('=', 1) #incase val has '='
					dict.__setitem__(self, key, val)
				
	def __setitem__(self, key, val):
		dict.__setitem__(self, key, val)
		with open(self._config, 'w') as fh:
			fh.write(key + "=" + val)
			fh.write('{0}={1}\n'.format(key,val))
			
cc = ConfigDict('config_file.txt')
