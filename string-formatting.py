# task from HackerRank
def formating(num):
    for i in range(1,num+1):
        print(f"{i}\t{format(i, 'o')}\t{format(i, 'x')}\t{format(i, 'b')}")

formating(17)
'''
num = int(input("Enter a decimal number: "))

oct1 = format(num, 'o')
print(oct1)
hex1 = format(num, 'x')
print(hex1)
binaer = {}
print(binaer)
'''
