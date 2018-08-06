#!/usr/bin/python

def gcd(n, m):
	min_num = n if n < m else m
	largestFactor = 1
	for i in range(1, min_num + 1):
		if n % i == 0 and m % i == 0:
			largestFactor = i
	return largestFactor

def get_int():
	return int(input("Enter the value of an Integer: "))

def main():
	n = get_int()
	m = get_int()
	print("gcd for", n , "and", m, " is", gcd(n, m))

main()
