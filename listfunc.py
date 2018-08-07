#!/usr/bin/python

def sum(lst):
	'''
	Returns the SUM of all
	List Values
	'''
	result = 0
	for item in lst:
		result += item
	return result

def clear(lst):
	'''
	Clears all of the values
	of List
	'''
	for i in range(len(lst)):
		lst[i] = 0

def random_list(n):
	import random
	result = []
	for i in range(n):
		rand = random.randrange(0, 100)
		result += [rand]
	return result

def main():
	a = [11, 23, 33, 45, 21, 11]

	print(a)

	print(sum(a))

	clear(a)

	print(a)
	
	print(random_list(10))

	print(a)

	
main()
