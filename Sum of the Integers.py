# How to Sum of the First N Positive Integers in Python
print('How to Sum of the First N Positive Integers in Python ?')
num = int(input('Enter your Number that you want: '))
total_sum = 0
for i in range(1,num+1):
    total_sum += i


print(total_sum)
