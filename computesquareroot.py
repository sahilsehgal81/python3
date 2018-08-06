#!/usr/bin/python

value = eval(input('Enter the number to find square root: '))

root = 1.0;

diff = root*root - value

while diff > 0.00000001 or diff < -0.00000001:
	root = (root + value/root) / 2
	print(root, 'squared is', root*root)
	diff = root*root - value
	
print('Square root of', value, "=", root)
