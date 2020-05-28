#!/usr/bin/python3
import sys
import subprocess
import os

for argument in sys.argv[1:]:
	print(f"{argument}: ",end = " ")
	S = os.popen('''stat -c "%s" {}'''.format(argument)).read()
	cmd = '''hexdump -n4 -s $(({}-4)) {} -e ' "%02x"' '''.format(S,argument)
	MAGIC = os.popen(cmd).read()
	if (MAGIC == '50504b50'):
		print("Yes (NS3)")
	elif (MAGIC == '50504b51'):
		print("Yes (NS4)")
	else:
		print("NO")

