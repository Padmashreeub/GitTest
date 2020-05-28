#! /usr/bin/python3
import json
import sys

user = {}

file = sys.argv[1]
with open('file',) as f:
	data = json.load(f)

username = data['request']['hops'][0]['username']
ip = data['request']['hops'][0]['client_addr']
size = data['request']['object_info']['size']

print(username , ip , size)

'''
if not 'username' in user :
	user['username'] = 'size'
else:
	user['username'] = user['username'] +size
	
topdict = dict(sorted(user.items(), key = lambda item: item[1], reverse = True)[:10]))

for k,v in topdict.items():
	print ("{},{}".format(k,v))
'''
