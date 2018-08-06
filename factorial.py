#!/usr/bin/python

def factorial(n):
	product = 1
	while n:
		product *= n
		n -= 1
	return product

def main():
	print("factorial 0:", factorial(0))
	print("factorial 1:", factorial(1))
	print("factorial 6:", factorial(2))
	print("factorial 9:", factorial(3))
	print("factorial -2:", factorial(4))
	print("factorial -2:", factorial(5))

main()
