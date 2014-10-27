#!/usr/bin/env python3
# Problem 2 
# https://github.com/KhalidGit/Project-Euler-solutions



def fib():
	count = 0
	a,b = 1,1
	while a < 4000000:
		if (a % 2 == 0):
			count += a 
		a,b = b, a+b
	print(count)
			
fib()