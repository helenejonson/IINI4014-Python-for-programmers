# Sort method that sorts by length and alphabetically
def sort(mylist):
    for passnum in range(len(mylist) - 1, 0, -1):
        for i in range(passnum):
            if len(mylist[i]) == len(mylist[i + 1]):
                if mylist[i] > mylist[i + 1]:
                    temp = mylist[i]
                    mylist[i] = mylist[i + 1]
                    mylist[i + 1] = temp
            if len(mylist[i]) > len(mylist[i + 1]):
                temp = mylist[i]
                mylist[i] = mylist[i + 1]
                mylist[i + 1] = temp

    return mylist


# Reads data from file
def readfile(name):
    mylist = []
    with open(name) as fp:
        for line in fp:
            myline = line.lower()
            for x in myline:
                if ord(x) < 97 or ord(x) > 122:
                    if ord(x) != 32:
                        myline = myline.replace(x, "")
                linelist = myline.split(" ")
            for x in linelist:
                mylist.append(x)
    return mylist


if __name__ == "__main__":
    print("Not sorted:")
    print(readfile("text"))
    print("Sorted:")
    print(sort(readfile("text")))
