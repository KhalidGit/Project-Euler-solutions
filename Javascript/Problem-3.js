//!/usr/bin/env javascript
// Problem 3
// https://github.com/KhalidGit/Project-Euler-solutions



// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143?

var n = 600851475143
var largest_factor = 1
var odds = 3

// remove any factors of 2 first
while (n % 2 == 0){
	largest_factor = 2
    n /= 2
}
    
// now look at odd factors
while (n != 1){
    while (n % odds === 0){
        largest_factor = odds
        n = n/odds
    }
    odds += 2
}

console.log(largest_factor)
