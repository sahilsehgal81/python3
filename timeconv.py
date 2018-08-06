#!/usr/bin/python

seconds = eval(input("Enter the time in seconds: "))

minutes = seconds // 60

hours = minutes // 60

microseconds = seconds * 60

print('You have entered ', seconds,'Seconds. Which are equals to ', minutes, ' Minutes. And equals to ', hours, ' hours. And equal to ', microseconds, ' ms.\n Thanks for the participation!\n Bye!')

#print(hours, ':', minutes, ':', seconds) 

tens = minutes // 10

ones = minutes % 10

print(tens, ones, ":", sep="", end="")
