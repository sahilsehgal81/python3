#!/usr/bin/python

def main():
	SUM = 0.0
	numbers = []
	entries = 5

	print("Enter", entries, "Numbers: ")
	for i in range(0, entries):
		num = eval(input("Enter number" + str(i) + ":"))
		SUM += num
		numbers += [num]

	print("The numbers are:", end=" ")
	for num in numbers:
		print(num, end=" ")

	print("Average: ", SUM/numbers )
