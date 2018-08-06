#!/uar/bin/python

from math import sqrt

def is_prime(n):
	root = sqrt(n)
	value = True

	trial_factor = 2

	while value and trial_factor <= root:
		value = (n % trial_factor != 0)
		trial_factor += 1
	return value
		
def main():
	max_value = int(input("Enter an Integer value: "))
	for value in range(2, max_value +1):
		if is_prime(value):
			print(value, end=" ")
	print()
main()

