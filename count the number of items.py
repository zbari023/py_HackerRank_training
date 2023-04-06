# How to count the number of items in a list in Python
print('How to count the number of items in a list in Python ?')
def countof(type,item):
    count = 0
    for i in type:
        if i == item:
            count = count + 1
    return count

print(countof((1,2,3,3),3))   # tuple ,list ,str