#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(coord1,coord2,round1):

    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]

    z1 = x2 - x1 
    z2 = y2 - y1

    u = (z1**2) + (z2**2)
    number = math.sqrt(u)
    ans = round(number,round1)
    return ans

x = distance((2,4) , (6,3) , 3)
print(x)