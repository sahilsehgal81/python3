#!/usr/bin/python

from random import randrange

#seed(23)

for i in range(0, 3):
	value = randrange(1, 6)

	print("+-------+")
	
	if value == 1:
		print("|        |")
		print("|   *    |")
		print("|        |")

	elif value == 2:
		print("| *      |")
		print("|        |")
		print("|      * |")

	elif value == 3:
		print("| *      |")
		print("|    *   |")
		print("|       *|")

	elif value == 4:
		print("| *     *|")
		print("|        |")
		print("| *     *|")

	elif value == 5:
		print("| *     *|")
		print("|    *   |")
		print("| *     *|")

	elif value == 6:
		print("|*  *   *|")
		print("|*  *   *|")
		print("|*  *   *|")
	else:
		print(" ***ERROR Illegal String*** ")

	print("+--------+")
