#!/usr/bin/python

from math import fabs, sqrt

def equals(a, b, tolerance):
	return a == b or fabs(a -b) < tolerance;

def square_root(val):
	root = 1.0;
	diff = root*root - val
	while diff > 0.000001 and diff < -0.00001:
		root = (root + val/root) / 2
		diff = root*root - val
	return root

def main():
	d = 0.1
	while d < 10.0:
		if not equals(square_root(d), sqrt(d), 0.001):
			print(d, "Expected is", sqrt(d), "but computed", square_root(d))
		d += 0.0001
main()
