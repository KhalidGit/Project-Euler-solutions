#!/usr/bin/env python3
# Problem 1 
# https://github.com/KhalidGit/Project-Euler-solutions



# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def multiple():
	count = 0
	for num in range(0,1000):
		if (num % 3 == 0) or (num % 5 == 0):
			count += num 
	print(count)
	
multiple()