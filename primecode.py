#!/usr/bin/python

from math import sqrt

def is_prime(n):
	factor = 2
	root = sqrt(n)

	while factor <= root:
		if n % factor == 0:
			return False;
	return True;
