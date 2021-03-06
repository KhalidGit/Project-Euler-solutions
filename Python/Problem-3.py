#!/usr/bin/env python3
# Problem 3
# https://github.com/KhalidGit/Project-Euler-solutions



# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?



def largest_prime_factor(n):

    largest_factor = 1

    # remove any factors of 2 first
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
 
    # now look at odd factors
    odds = 3
    while n != 1:
        while n % odds == 0:
            largest_factor = odds
            n = n/odds
        odds += 2

    return largest_factor
 

print(largest_prime_factor(600851475143))