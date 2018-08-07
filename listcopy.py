#!/usr/bin/python

def list_copy(lst):
	result = []
	for list in lst:
		result += [list]
	return result

def main():
	a = [10, 20, 30, 40]
	b = list_copy(a)

	print("a = ", a, " b = ", b)

	print("Is", a, "equals to ", b, "?", sep="", end=" ")
	print(a == b)

	print("Is", a, "an alias of", b, "?", sep="", end=" ")
	print(a is b)

	b[2] = 35

	print("a = ", a, "and b = ", b)

main()
		
