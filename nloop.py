#!/usr/bin/python

def fun(n):
	result = 0
	while n:
		result += n
		n--
	return result

fun(5)
