# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
print('Joining a string: ')


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line


if __name__ == '__main__':
    line = input('Enter the sentence: ')
    result = split_and_join(line)
    print(result)