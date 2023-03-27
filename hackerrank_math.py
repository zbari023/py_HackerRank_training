import math
import cmath
for i in range(1,5):
  print(f'{i}'*i)
print('**** other way ****')
for j in range(1,5): # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**j)//9)*j)
print('*********')
AB = int(input('enter AB= '))
BC = int(input('enter BC= '))

AC = math.sqrt((pow(AB,2))+pow(AB,2))
MC = int(AC/2)
phi = math.asin(MC/BC)
phi_deg = math.degrees(phi)

print(f"{math.ceil(phi_deg)}\N{DEGREE SIGN}")

print('*********')

z = complex(input('enter your complex number: '))
real = z.real
img = z.imag

print(math.sqrt( (real**2 + img**2 )))
phi =  math.atan(img / real)
print(abs(complex(phi)) )

print('**********')
a = int(input('a= '))
b = int(input('b= '))
print(a//b)
print(a%b)
tuple_add=(a//b,a%b)
print(tuple_add)
'''
def comtocer(x,y):
    z = complex(x, y)
    r = math.sqrt(pow(x, 2) + pow(y, 2))
    phi = math.atan(y / x)
    print(r)
    print(phi)

comtocer(1,2)
'''
