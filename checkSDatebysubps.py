#!/usr/bin/python3
import subprocess
import sys
from datetime import datetime

format = "%Y/%m/%d-%H:%M:%S"
print(f"Local date: {(datetime.now()).strftime(format)}")

arglen = len(sys.argv)

if (arglen > 1):
	for i in range(1, arglen):
		try :
			cmd = "curl -sD - -o /dev/null {}|grep -i date".format(sys.argv[i])
			p = subprocess.Popen(cmd , stdout = subprocess.PIPE , stderr = subprocess.DEVNULL , shell = True)
			str = p.communicate(timeout = 5)[0].decode()
			dtstr = str[6:].strip()
			dtobj = datetime.strptime(dtstr,'%a, %d %b %Y %H:%M:%S %Z')
			print(f"{sys.argv[i]}: {dtobj.strftime(format)}")
		except :
			print (f"{sys.argv[i]}: cannot get date")

else:
 	print("you did't pass any arguments")




