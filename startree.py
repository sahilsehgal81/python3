#!/usr/bin/python

val = eval(input("Enter the value of Tree towers: "))

row = 0

while row < val:
	count = 0
	while count < val - row:
		print(end=" ")
		count += 1

	count = 0
	while count < 2*row + 1:
		print(end="*")
		count += 1
	print()
	row += 1
