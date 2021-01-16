def initals(input):
    init = []
    inputlist = input.split(' ')
    for x in inputlist:
        letter = x[0].upper()
        init.append(letter)
    return ''.join(init)


if __name__ == '__main__':
    x = input("Name: ")
    print("Init:", initals(x))
