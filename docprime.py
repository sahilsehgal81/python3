#!/usr/bin/python

'''
Contains the definition of the is_prime function
'''

from math import sqrt

def is_prime(n):
	'''
        Returns true if non-negative integer n is Prime;
	otherwise, returns False.
	'''
	factor = 2
	root = sqrt(n)

	while factor <= root:
		if n % factor == 0:
			return False;
		else:
			return True;
