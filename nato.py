#!/usr/bin/python3
import sys

nato = {'a':'Alfa','b':'Bravo','c':'Charlie','d':'Delta','e':'Echo','f':'Foxtrot','g':'Golf','h':'Hotel','i':'India','j':'Juliett','k':'Kilo','l':'Lima','m':'Mike','n':'November','o':'Oscar','p':'Papa','q':'Quebec','r':'Romeo','s':'Sierra','t':'Tango','u':'Uniform','v':'Victor','w':'Whiskey','x':'X-ray','y':'Yankee','z':'Zulu',}

a = sys.argv
arglen = len(a)
if arglen > 1:
	for argument in range(1,arglen):
		if a[argument].isalpha():
			str=a[argument].lower()
			for pos in str:
				print(nato[str[pos]], end = " ")
		else :
			print("{} wrong str,contains non alphabets".format(a[i]))
		print('')
else:
 	print("you did't pass any argument")
