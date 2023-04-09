# How to Turn a list into a string in Python
def turn_list(listing):
    result=''
    for i in listing:
        result = result + str(i)

    return ' '.join(result)
print(turn_list([1,2,3,4,5]))