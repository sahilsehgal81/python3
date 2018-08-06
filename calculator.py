#!/usr/bin/python

def info():
	print("Type 'A' for Adding two numbers:\n")
	print("Type 'S' for Subtracting two numbers:\n")
	print("Type 'H' for finding the help menu: \n")
	print("Type 'P' for printing the result\n")

def menu():
	return input("For Add press: 'A', for Help type 'H' and for Print type 'P': ")

def main():
	result = 0.0
	while True:
		value = menu()

		if value == "A" or value == "a":
			arg1 = float(input("Add ARG1: "))
			arg2 = float(input("Add ARG2: "))
			result = arg1 + arg2
			print(result)
		elif value == "H" or value == "h":
			info()
		elif value == "P" or value == "p":
			print(result)
main()
