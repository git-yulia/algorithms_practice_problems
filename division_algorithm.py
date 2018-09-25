# Analysis of Algorithms
# Practice Assignment 2
# Author: Julia Maliauka
# Quiz 3 - The Division Algorithm
# (Problem 1.3 in the textbook)

import sys 

# Problem prompt: estimate the complexity of the running time of the Divsion algorithm in terms of Big O notation. 

# PRE-CONDITION:
# x >= 0 && y > 0 && x, y in N

x = int(input("Please input x: "))
y = int(input("Please input y: "))

q = 0
r = x

while y <= r:
    r = r - y
    q = q + 1

print("quotient(x,y) is ", q)
print("remainder(x,y) is ", r)

# POST-CONDITION: x = (q * y) + r

# What is the loop invariant here? 
# loop invariants are true for each iteration of a loop
# (both before and after the loop runs)

# our loop invariant here is:
"""
x = (q * y) + r
"""

# Now what is the complexity of the running time in Big-O notation?


