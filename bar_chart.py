# How to Create a bar chart from a given list of integers in Python
def histo(items):
    for n in items:
        out = ''
        while n > 0:
            out += '*'
            n =n-1
        print(out)
histo([10,2,3,4,5])
'''
def histogram(listing):
    listing = listing.split(',') # darstellung der input
    l =[]                        # darstellung der neuen list
    for i in listing:
        l.append(int(i))
    return l, tuple(l)         # to make the output as result --> '\n'.join(l)



print(histogram('1,2,3,4,5'))
'''
