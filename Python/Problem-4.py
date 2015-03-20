#!/usr/bin/env python3
# Problem 3
# https://github.com/KhalidGit/Project-Euler-solutions



#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.



def palindrome_product():
	a = 999
	b = 999
	pals = []
	number = 1
	while a > 99:
		while b > 99:
			number = a * b
			if palindrome_checker(number) == True:
				pals.append(number)
			b -= 1

		a -= 1
		b = 999
	pals.sort()
	return(pals[-1])

def palindrome_checker(m):
	bool = False
	stringed_number = str(m)
	if len(stringed_number) == 5:
		if stringed_number[0] == stringed_number[-1] and stringed_number[1] == stringed_number[-2]:
			bool = True
			return bool
		return bool
	else:
		if stringed_number[0] == stringed_number[-1] and stringed_number[1] == stringed_number[-2] and stringed_number[2] == stringed_number[-3]:
			bool = True
			return bool
		return bool

print(palindrome_product())




