#!/usr/bin/python

def userlist():
	result = []
	listval = 0

	while listval >= 0:
		listval = int(input("Enter the numbers to be added as list: "))
		if listval >= 0:
			result = result + [listval]
	return result

def main():
	col = userlist()
	print(col)
main()
