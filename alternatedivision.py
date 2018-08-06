#!/usr/bin/python

divident, divisor = eval(input('Enter a Divisor and Divident Value: '))

if divisor != 0:
	quotient = divident/divisor
	print('Here Divisor is', divident, '. Divident is', divisor, '. And Quotient is ', quotient)
	print('\nOr in other words\n');
	print(divident, '/', divisor, '=', quotient,'\n')
print('Program Finished!')
