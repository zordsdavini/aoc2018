import sys

f = open('input.txt', 'r')
twices = {0: True}
sum = 0
while True:
    for row in f:
        sum += (int(row))
        print(sum)
        if sum in twices:
            print('-->> ', sum)
            sys.exit()
        twices[sum] = True
    f.seek(0)
