#!/usr/bin/python

print("      1   2   3   4   5   6   7   8   9   10")
print("  +-------------------------------------------")

for row in range(1, 11):
	if row < 10:
		print(" ", end="")
	
	print(row, "|", end="")

	for column in range(1, 11):
		multiple = row*column;
#		if multiple < 100:
#			print(end=" ")
#		if multiple < 10:
#			print(end=" ")
		print(multiple, end=" ")
	print()	
