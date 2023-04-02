# How to find average of N numbers in Python
print('How to find average of N numbers in Python ?')
limit = int(input('Enter how many Numbers do you want: '))
total_sum = 0
for i in range(limit):
    numbers = float(input('Enter your numbers: '))
    total_sum += numbers
print(f'The average of your Numbers is = {total_sum/limit}')