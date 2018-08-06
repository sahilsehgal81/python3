#!/usr/bin/python

from time import clock

print("Enter your name: ", end="")
start_time = clock()
name = input()
time_taken = clock() - start_time

print("You've entered Name: ", name, ".And it took you ", time_taken, "time to write.")
