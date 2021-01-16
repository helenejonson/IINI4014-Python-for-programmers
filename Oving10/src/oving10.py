import os
import re


class textAnalyzer:
    def __init__(self):
        self.text = []
        self.path = ''

    def readfile(self, file):
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in [f for f in filenames if f.endswith(".txt")]:
                if file == filename:
                    self.path = os.path.join(dirpath, filename)
        f = open(self.path)
        r = f.read()
        sentences = r.split('.')
        for x in range(len(sentences)):
            cleanline = self.clean(sentences[x])
            sentences[x] = cleanline

        self.text = sentences

    def clean(self, line):
        line = re.sub('[^A-Za-z0-9]+', " ", line).lower().replace("\n", "").split(' ')
        count = 0
        while count < len(line):
            if line[count] == '':
                line.pop(count)
                count = count - 1
            count += 1
        return line

    def sentencelengthwords(self):
        sentencelength = {}
        for x in range(len(self.text)):
            sentencelength[x + 1] = len(self.text[x])
        print(sentencelength)

    # How many words have higher use than the limit
    # How many different words are there total
    def easywords(self, limit):
        words = self.difwords()
        wordsoverlimit = 0
        for key in words:
            if words[key] >= limit:
                wordsoverlimit += 1
        percentage = wordsoverlimit / len(words) * 100
        return percentage

    def hardwords(self, limit):
        words = self.difwords()
        wordsoverlimit = 0
        for key in words:
            if words[key] <= limit:
                wordsoverlimit += 1
        percentage = wordsoverlimit / len(words) * 100
        return percentage

    def presdiffwords(self):
        words = self.difwords()
        totalwords = 0
        for key in words:
            totalwords += words[key]
        percentage = len(words) / totalwords * 100
        return percentage

    def sentenceperparagraph(self):
        paragraph = {}
        f = open(self.path)
        r = f.read()
        sentences = r.split('\n\n')
        counter = 0
        for x in range(len(sentences)):
            sent = sentences[x].split('.')
            count = 0
            while count < len(sent):
                if sent[count] == '':
                    sent.pop(count)
                    count = count - 1
                count += 1
            if len(sent) > 0:
                a = len(sent)
                paragraph[counter + 1] = len(sent)
                counter += 1
        return paragraph

    def difwords(self):
        diffwords = {}
        for line in self.text:
            for word in line:
                if word in diffwords:
                    diffwords[word] += 1
                else:
                    diffwords[word] = 1
        return diffwords


if __name__ == '__main__':
    ta = textAnalyzer()
    ta.readfile('pg5200.txt')
    print('{Sentence nr : words}')
    ta.sentencelengthwords()
    print('Percentage often used words:')
    print(ta.easywords(10))
    print('Percentage less used words:')
    print(ta.hardwords(2))
    print('Percentage of total words to unique words:')
    print(ta.presdiffwords())
    print(ta.sentenceperparagraph())
