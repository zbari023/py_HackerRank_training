# How to Create a bar chart from a given list of integers in Python

def histogram(listing):
    listing = listing.split(',') # darstellung der input
    l =[]                        # darstellung der neuen list
    for i in listing:
        l.append(int(i))
    return l, tuple(l)         # to make the output as result --> '\n'.join(l)



print(histogram('1,2,3,4,5'))