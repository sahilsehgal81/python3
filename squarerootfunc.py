#!/usr/bin/python

def squareroot(val):
	root = 1.0
	diff = root*root - val
	while diff > 0.0000001 or diff < -0.0000001:
		root = (root + val/root)/2
		diff = root*root -val
	return root

def main():
	num = float(input("Enter the value of number: "))
	print("The square root of ", num, "is: ", squareroot(num))
main()
