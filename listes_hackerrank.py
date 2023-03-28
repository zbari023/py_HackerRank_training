# convert to list
N = input('Enter your numbers with "," between its to convert its to list: ')
x=N.split(',')
l=[]
for i in x:
    l.append(int(i))
print(l)