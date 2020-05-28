#! /usr/bin/python3
import json
import sys
import re

user = {}
userip = {}

if (len(sys.argv) > 1):
	with open(sys.argv[1]) as f:
		filedata = f.readlines()
elif not(sys.stdin.isatty()):
	filedata = sys.stdin.readlines()
else:
	print("neither argument or stdin is passed")
	sys.exit(1)

for jsonline in filedata:
	try:
		jsondata = json.loads(jsonline)
		if(jsondata['request']['request_info']['xaaa_action'] == 'upload'):
			username = jsondata['request']['hops'][0]['username']
			ip = jsondata['request']['hops'][0]['client_addr']
			size = jsondata['request']['object_info']['size']

			if not (username in user):
				user[username] = size
				userip[username] = ip
			else:
				user[username] = user[username] +size
				if not (ip in userip[username]):
					userip[username] = "multiple"
				
	except:
		continue
	
topdict = dict(sorted(user.items(), key = lambda item: item[1], reverse = True)[:10])

for k,v in topdict.items():
	unit = "byte"
	size = topdict[k]
	if (size >1073741824):
		size = topdict[k] / 1073741824
		unit = "GB"
	elif (size >1048576):
		size = topdict[k] / 1048576
		unit = "MB"
	elif (size >1024):
		size = topdict[k] / 1024
		unit = "KB"
	print(f"{k} :{size:.1f}{unit}", end = " ")

	ipstatus = "single" if re.search(r"[0-9.]" , userip[k]) else "Multiple"
	print (f"{ipstatus} ip")
	print(userip[k])

