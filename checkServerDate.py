#!/usr/bin/python3
import subprocess
import sys
import requests
from datetime import datetime

format = "%Y/%m/%d-%H:%M:%S"
print(f"Local date: {(datetime.now()).strftime(format)}")

if len(sys.argv) < 2:
	print ("you did't pass any arguments")
	sys.exit(0)

for argument in sys.argv[1:]:
	try :
		pos = argument.find("https://")
		url = argument if pos == 0 else "https://"+argument
		resultdate = requests.get(url , timeout = 1).headers['date']
		dtobj = datetime.strptime(resultdate,'%a, %d %b %Y %H:%M:%S %Z')
		print(f"{argument}: {dtobj.strftime(format)}")
		
	except :
		print (f"{argument}: cannot get date")




