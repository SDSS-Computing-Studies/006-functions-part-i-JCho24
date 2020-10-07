#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""

def largest(listt):
    listt.sort()
    ans = listt[-1]
    return ans

a = largest([1,7,2,19,5,6])
print(a)