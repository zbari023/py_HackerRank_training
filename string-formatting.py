# task from HackerRank
def print_formatted(number):
    # your code goes here
    l = len(bin(number)[2::])
    for i in range(1,number+1):
        print(str(i).rjust(l),oct(i)[2::].rjust(l),hex(i)[2::].rjust(l).upper(),bin(i)[2::].rjust(l))

print_formatted(4)
'''
def formating(num):
    for i in range(1,num+1):
        print(f"{i}\t{format(i, 'o')}\t{format(i, 'x')}\t{format(i, 'b')}")

formating(1)
'''
'''
num = int(input("Enter a decimal number: "))

oct1 = format(num, 'o')
print(oct1)
hex1 = format(num, 'x')
print(hex1)
binaer = {}
print(binaer)
'''
