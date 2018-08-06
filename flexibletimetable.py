#!/usr/bin/python

MAX = 20

print(end="    ")

for row in range(1, MAX + 1):
	print(end=" %2i " % row)
print()

print(end="   +")
for row in range(1, MAX + 1):
	print(end="----")
print()

for row in range(1, MAX + 1):
	print(end="%2i | " % row)
	for column in range(1, MAX + 1):
		multiple = row*column
		print(end="%3i " % multiple)
	print() 
