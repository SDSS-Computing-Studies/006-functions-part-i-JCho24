#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(num):
    ans = num % 2
    if ans == 0 or ans == 1:
        return True
    else:
        return False

a = isInteger(3.5)
print(a)