#!/usr/bin/python

value = eval(input("Enter the tree layer: "))

row = 0

while row < value:
	count = 0
	while count < value - row:
		print(end=" ")
		count += 1

	count = 0
	while count < 2*row - 1:
		print(end="*")
		count += 1
	print()
	row += 1
