f = open('input.txt', 'r')
twice = 0
triple = 0
for row in f:
    row = row.strip('\t\n\r')

    counts = {}
    for l in row:
        if l not in counts:
            counts[l] = 0
        counts[l] += 1

    for l in counts:
        if counts[l] == 2:
            twice += 1
            break

    for l in counts:
        if counts[l] == 3:
            triple += 1
            break

print(twice*triple)
