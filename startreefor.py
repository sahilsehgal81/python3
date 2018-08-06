#!/usr/bin/python

value = eval(input("Enter the layer of tree: "))

for row in range(value):
	for count in range(value - row):
		print(sep=" ")

	for count in range(2*row + 1):
		print(sep="*")

	print()
