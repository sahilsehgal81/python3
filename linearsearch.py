#!/usr/bin/python

def locate(lst, seek):
	'''
	lst is the list of elements where seek
	is the index element to locate within lst 
	list
	'''
	for i in range(len(lst)):
		if lst[i] == seek:
			return i
	return None

def format(i):
	'''
	print i in the format of 4-space field.
	if i is greater than 9999, prints 5 stars
	'''
	if i > 9999:
		print("*****")
	else:
		print("%4d" % i)

def show(lst):
	'''
	shows the contents of list
	'''
	for item in lst:
		print("%4d" % item, end="")
	print()

def draw_arrow(value , n):
	'''
	print an arrow to value which is an element of list.
	n specifies the horizontal offset of the arrow
	'''
	print(("%" + str(n) + "s") % "    ^     ")
	print(("%" + str(n) + "s") % "    |     ")
	print(("%" + str(n) + "s%i") % ("    +-- ", value))

def display(lst, value):
	'''
	Draws an ASCII art Arrow showing where
	the value is within list.
	lst is the list.
	value is the element to locate.
	'''
	show(lst)
	position = locate(lst, value)
	if position != None:
		position = 4*position + 7;
		draw_arrow(value, position)
	else:
		print("(", value, " not in list)", sep='')
	print()

def main():
	a = [100, 22, 33, 45, 6, 44, 67, 23, 4, 5, 6, 7]
	display(a, 13)
	display(a, 2)
	display(a, 100)
	display(a, 22)
	display(a, 7)

main()
