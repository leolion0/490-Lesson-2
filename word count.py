import string
infile = open("input.txt", 'r')
words = dict()
line = infile.readline()

while line !="":
    line = line.translate(str.maketrans('', '', string.punctuation + '1234567890' + '\n'))
    line = line.lower()
    lineList = line.split(' ')
    for i in lineList:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    line = infile.readline()

infile.close()
infile = open('input.txt', 'a')
infile.write('\n\n')
for key, val in words.items():
    if key is not None:
        infile.write(str(key) + ": " + str(val) + "\n")


# print(words)