#!/usr/bin/python

def main():

	data = [10, 20, 30, 40, 50]

	print(data[-1])
	print(data[-2])
	print(data[-3])
	print(data[-4])
	print(data[-5])

	print("----------")

#	print(len(data))

	for i in range(-1, -len(data) -1, -1):
		print(data[i], end=" ")
	print()
main()
