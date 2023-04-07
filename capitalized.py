def solve(s):
    l=[]
    k = s.split(' ')
    for i in k:
        l.append(i.capitalize())
    return ' '.join(l)
print(solve('ziad bari'))   # Ziad Bari