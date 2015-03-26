#!/usr/bin/env Ruby
# Problem 1 
# https://github.com/KhalidGit/Project-Euler-solutions



# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiple_of_three?(n)
  n % 3 == 0
end

def multiple_of_five?(n)
  n % 5 == 0
end

def acceptable(n)
  multiple_of_three?(n) || multiple_of_five?(n)
end

p (0..999).select { |n| acceptable(n) }.reduce(:+)