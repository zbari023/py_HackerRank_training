# How to find Area of a Circle in Python
print('How to find Area of a Circle in Python ?')
import math

def cirArea(r):
    if r >= 0:
        return math.pi * pow(r, 2)
    else:
        print('The radius should be positiv Number')

print(cirArea(1))
