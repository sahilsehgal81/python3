#!/usr/bin/python

def main():
	ENTRIES = 5
	SUM = 0.0
	NUMBER = []

	print("Please enter", ENTRIES, "numbers: ")
	for i in range(0, ENTRIES):
		num = eval(input("Enter number " + str(i) + ": "))
		SUM += num
		NUMBER += [num]

	print(end="Number entered: ")
	for num in NUMBER:
		print(num, end=" ")
	print()
	
	
	print("Average: ", SUM/ENTRIES)
main()
