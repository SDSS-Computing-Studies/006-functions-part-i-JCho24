#! python3
"""
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10
(2 points)
"""
import math

def factors(a):
    alist = []
    for i in range(1,a + 1):
        b = a / i
        b = int(b)
        if a % b == 0:
            alist.append(b)
            
    
    alist.sort()
    newlist = list(set(alist))
    x = newlist[0:a]
    return x

y = factors(12)
print(y)