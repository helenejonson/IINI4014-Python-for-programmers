import os
import re


def getwordfreqs(file):
    allwords = {}
    f = open(findfile(file))
    for x in f:
        line = clean(x)
        for i in line:
            if i in allwords:
                allwords[i] += 1
            else:
                allwords[i] = 1
    print(allwords)


def getwordsline(file, word):
    lines = []
    f = open(findfile(file))
    count = 1
    for x in f:
        line = clean(x)
        if word in line:
            lines.append(count)
        count += 1
    print(lines)


def findfile(file):
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(".txt")]:
            if file == filename:
                return os.path.join(dirpath, filename)


def clean(line):
    line = re.sub('[^A-Za-z0-9]+', " ", line).lower().replace("\n", "").split(' ')
    count = 0
    while count < len(line):
        if line[count] == '':
            line.pop(count)
            count = count - 1
        count += 1
    return line


if __name__ == '__main__':
    getwordfreqs('pg5200.txt')
    getwordsline('pg5200.txt', 'time')
