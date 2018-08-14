#!/usr/bin/python

class Rational:
	'''
	Represents a rational number (fraction)
	'''
	def __init__(self, num, den):
		self.__numerator = num
		if den != 0:
			self.__denominator = den
		else:
			print("Denominator is not Non-Zero")
			from sys import exit
			exit(1)

	def getnumerator(self):
		return self.__numerator

	def getdenominator(self):
		return self.__denominator

	def setnumerator(self, n):
		self.__numerator = n

	def setdenominator(self, d):
		if d != 0:
			self.__denominator = d
		else:
			print("Numerator is Non Zero")
			from sys import exit
			exit(1)
	def __str__(self):
		return  str(self.getnumerator()) + "/" + str(self.getdenominator())

def main():
	fract1 = Rational(1, 2)
	fract2 = Rational(2, 3)
	print("Fract1 is", fract1)
	print("Fract2 is", fract2)
	fract1.setnumerator(5)
	fract1.setdenominator(7)
	fract2.setnumerator(10)
	fract2.setdenominator(4)
	print("Fract1 =", fract1)
	print("Fract2 = ", fract2)

main()
