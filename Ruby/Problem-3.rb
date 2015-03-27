#!/usr/bin/env Ruby
# Problem 3
# https://github.com/KhalidGit/Project-Euler-solutions



# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

number = 600851475143

def get_prime(n)
  (2..n).each do |i|
    if i == n
      return n
    elsif n % i == 0
      return get_prime(n/i)
    end
  end
end

puts get_prime(number)
