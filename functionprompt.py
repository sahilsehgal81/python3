#!/usr/bin/python

def prompt(n):
	value = int(input("Enter the value of integer: "))
	return value
print("This program adds two integers")
value1 = prompt(1)
value2 = prompt(2)
sum = value1 + value2
print("Sum of", value1, "+", value2, "is", sum)
