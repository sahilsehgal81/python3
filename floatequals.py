#!/usr/bin/python
from math import fabs

def equal(a, b, tolerance):
	return a == b or fabs(a - b) < tolerance;

def main():
	i = 0.0
	while not equal(i, 1.0, 0.01):
		print("i= ",i)
		i += 0.1
main()
