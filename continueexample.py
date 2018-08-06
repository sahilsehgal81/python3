#!/usr/bin/python

done = False
sum = 0
print("Please enter a number (999 to Quit)")

while not done:
	value = eval(input())
	if value < 0:
		print("Value Entered", value, "is a Negative Number")
		continue
	if value != 999:
		print("The Value goes on here: ")
		sum += value
	else:
		done = (value == 999);
print("Sum is =", sum)				

