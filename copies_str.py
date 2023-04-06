# How to Get a string which is n copies of a given string in Python
print('How to Get a string which is n copies of a given string in Python ?')
def copy_str(given_str,n):
    res = ""
    for i in range(n):
        res = res + given_str
    return int(res) , int(res[::-1])

print(copy_str("12345",1))