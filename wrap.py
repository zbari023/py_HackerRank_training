import textwrap

def wrap(string, max_width):
    return ("\n").join(textwrap.wrap(string, max_width))
print(wrap('qweqrqwrwterte',4))