#!/usr/bin/python

entry = 0
sum = 0

print("Enter the positive numbers to extend list and Negative number to end program: ")

while entry >= 0:
	entry = eval(input())
	if entry >= 0:
		sum += entry
print("Sum =", sum)
