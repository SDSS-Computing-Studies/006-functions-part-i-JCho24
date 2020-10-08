#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""

import math

def hypotenuse(a,b,c):
    if c == True:
        ab = (a**2) + (b**2)
        ans = math.sqrt(ab)
        return ans
        
    elif c == False:
        abc = []
        abc.append(a)
        abc.append(b)
        abc.sort()
        d = abc[0]
        e = abc[-1]
        f = (e**2) - (d**2)
        ans = math.sqrt(f)
        return ans

x = hypotenuse(5,13,False)
print(x)