# How to find n copies of the first 2 characters of a given string in Python
def make_copy(string,n):
    result = ""
    for i in range(n):
        result = result + string[0] + string[1]
    return result
print(make_copy("abcd",10))