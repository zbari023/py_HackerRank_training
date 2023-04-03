# How to create a list and tuple with comma separated numbers in Python
print('How to create a list and tuple with comma separated numbers in Python ?')
elements = input('Enter your numbers: ')
elements = elements.split(',')        # as separators
listing = []
for i in elements:
    listing.append(int(i))
print(listing)         # [1, 2, 3, 4, 5]
print(tuple(listing))  # to a tuple  (1, 2, 3, 4, 5)

