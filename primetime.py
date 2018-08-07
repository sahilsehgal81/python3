#1/usr/bin/python

from time import clock
from math import sqrt

def find_prime(n):

	start = clock()
	count = 0
	for val in range(2, n):
		root = sqrt(val) + 1
		trial_factor = 2
		result = True
		while result and trial_factor <= root:
			result = (val%trial_factor != 0)
			trial_factor += 1
		if result:
			count += 1
			
	stop = clock()
	print("Count =", count, "Elapsed time:", stop - start, "seconds")

find_prime(1000000)
