#!/usr/bin/python

entry = 0
sum = 0

print("Please enter the Value: ")

while True:
	entry = eval(input())
	if entry < 0:
		break
	sum += entry
print("Sum is", sum)
	
