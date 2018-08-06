#!/usr/bin/python

from random import seed, randrange

seed(23)

for i in range(1, 100):
	print(randrange(1, 1000), end=" ")
print()
