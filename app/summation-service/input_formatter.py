
def removeQuotes(text):
    text = text.replace("\"", "\'")
    text = text.replace("\n", " ")
    text = text.replace("\r", "")
    print text
    return text

def removeSpecialChars(text):
    text = text.replace('&', 'and')
    return text

def process(text):
    text = removeQuotes(text)
    text = removeSpecialChars(text)
    return text

def main(path):
    f = open(path, 'r')
    text = f.read()
    f.close()

    text = process(text)

    f = open(path + 'processed.txt', 'w')
    f.write(text)
    f.close()
    return True


import os
from os.path import isfile, join

onlyfiles = []
for file in os.listdir("resources/bodies"):
    if file.endswith(".txt"):
        onlyfiles.append(os.path.join("resources/bodies", file))

for path in onlyfiles:
    main(path)
