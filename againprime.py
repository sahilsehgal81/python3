#!/usr/bin/python

from math import sqrt
from time import clock

def find_prime_num(n):

	start = clock()
	count = 0
	for val in range(2, n):

		trial_factor = 2
		result = True
		root = sqrt(n) + 1
	
	
		while result and trial_factor <= root:
			result = (val%trial_factor != 0)
			trial_factor += 1
		if result:
			count += 1

	stop = clock()
	print("Count: ", count, "Elapsed time:", stop - start, "seconds")

find_prime_num(10000)
