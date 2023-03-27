import math
for i in range(1,5):
  print(f'{i}'*i)
print('**** other way ****')
for j in range(1,5): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**j)//9)*j)

AB = int(input('enter AB= '))
BC = int(input('enter BC= '))

AC = math.sqrt((pow(AB,2))+pow(AB,2))
MC = int(AC/2)
phi = math.asin(MC/BC)
phi_deg = math.degrees(phi)

print(f"{math.ceil(phi_deg)}\N{DEGREE SIGN}")