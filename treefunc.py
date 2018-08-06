#!/usr/bin/python

def tree(height):
	row = 0
	while row < height:
		count = 0
		while count < height - row:
			print(end=" ")
			count += 1

		count = 0
		while count < 2*row + 1:
			print(end="*")
			count += 1

		print()
		row += 1

def main():
	height = int(input("Enter the value of height of Tree: "))
	tree(height)

main()
