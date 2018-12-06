import sys

f = open('input.txt', 'r')
words = []
for row in f:
    row = row.strip('\t\n\r')
    print(row)

    for w in words:
        correct = ''
        count = 0
        for i, l in enumerate(w):
            if row[i] != l:
                count += 1
            else:
                correct += l
        if count == 1:
            print(correct)
            sys.exit()
    words.append(row)
