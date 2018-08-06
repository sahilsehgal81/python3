#!/usr/bin/python

def getvalue(first, second):
	if first > second:
		first, second = second, first

	value = int(input("Please enter integers ranging between " + str(first) + "..." + str(second) + ":"))
	while value < first or value > second:
		print(value, "is not between the range. Please try again!")
		value = int(input("Please enter values again: "))
	return value;

def main():
	print(getvalue(10, 20))
	print(getvalue(11, 10))
	print(getvalue(1, -1))
main()
