#!/usr/bin/env python3
# Problem 3
# https://github.com/KhalidGit/Project-Euler-solutions

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# ---------------incorrect solution so far. Correct solution (done by hand) == 232,792,560------------

def list_builder(n):
	list = []
	for i in range(n):
		list.append(i + 1)
	return list



def LCM(n):
	list = list_builder(n)
	mult = 1
	for i in range(0, len(list)-1):
		multiplier = list[i] # 1 for the first iteration 
		for j in range(1, len(list)):
			action = list[i] # 2 for the first iteration
			if (action%multiplier) == 0:
				reduced = (action//multiplier)
				list[i+1] = reduced
				print('reduced')
				print(list)
	
	# for k in range(0, len(list)):
	#     mult *= list[i]
	# return list
	    

lcm= LCM(20)
print(lcm)
