#!/usr/bin/python
from random import randrange

A = [0, 1, 2, 3, 4, 5, 6, 7]

n = len(A)
print("Length of List: ", n)

for i in range(n - 1):
#	print("Value for i: ", i)
	small = i
	for j in range(i + 1, n):
		print("Value for A[j] ",A[j], ". Value of A[small]", A[small])
		if A[j] < A[small]:
			small = j
			print("Small :", small)
			print("J: ", j)

	if small != i:
		print("Small: ", small)
		print("i : ", i)
