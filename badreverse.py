#!/usr/bin/python

def eval_list():
	in_val = 0
	result = []

	while in_val >= 0:
		in_val = eval(input("Enter the values [-1 to QUIT]: "))
		if in_val >= 0:
			result += [in_val]
	return result

def main():
	col = eval_list()

	for i in range(len(col) - 1, -1, -1):
		print(col[i], end=" ")
	print()

main()
		
