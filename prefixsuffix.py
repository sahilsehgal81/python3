#!/usr/bin/python

a = [1, 2, 3, 4, 5, 6, 7, 8]

print("Prefix of a : ")
for i in range(0, len(a) +1):
	print("<", a[0:i], ">")

print("Suffix of a: ")
for i in range(0, len(a) + 1):
	print("<", a[i:len(a)], ">")
