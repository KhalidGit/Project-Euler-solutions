//!/usr/bin/env javascript 
// Problem 2 
// https://github.com/KhalidGit/Project-Euler-solutions



// Each new term in the Fibonacci sequence is generated by adding the previous two terms.
// By starting with 1 and 2, the first 10 terms will be:

// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

// By considering the terms in the Fibonacci sequence whose values do not exceed four million,
// find the sum of the even-valued terms.



count = 0
var a = 1
var b = 1

while (a < 4000000){
    if (a%2 === 0){
        count += a 
    }
    var [a, b] = [b, a+b];
}

	

console.log(count)