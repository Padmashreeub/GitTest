#!/usr/bin/python3

import sys
import sqlite3
import re

if not(len(sys.argv) in range(2,7)):
	print("Wrong number of arguments")
	sys.exit(1)
 # Open the database
conn = sqlite3.connect('query.db')

# For each cpcode provided in command line, try to lookup the associated accountname
c = conn.cursor()

for cpcode in sys.argv[1:]:
	if(re.match('^\d+$', cpcode) and len(cpcode)<8):
		c.execute("SELECT accountname FROM cpmap where cpcode = %s" % cpcode)
		row = c.fetchone()
		if row is None:
			print("%s: Doesn't exists"% (cpcode))
		else:
			print("%s: %s"% (cpcode, row[0]))
	else:
		print("Wrong input")

