"""
For this case it is imposible to get answer by counting each generation.
At first I found that there are only 508 patterns and later it goes only one but with shift to the right side.
Next I found that each generation (startin from 508 iteration) grows by 36 in sum.
Then generated 2000 iterations and did some arithmetics:
In [18]: 50000000000 - 2000
Out[18]: 49999998000
In [19]: _*36
Out[19]: 1799999928000
In [20]: _+71458    <--- the sum in 2000th generation
Out[20]: 1799999999458

Used code for research left commented out

p.s. it has 1 and 2 part in one. To get 1st part - big_count should be 20.
"""

init = '#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............'

data = {
    '##...': '.',
    '##.##': '.',
    '.#.#.': '#',
    '#..#.': '.',
    '#.###': '#',
    '.###.': '.',
    '#.#..': '.',
    '##..#': '.',
    '.....': '.',
    '...#.': '.',
    '.#..#': '.',
    '####.': '#',
    '...##': '#',
    '..###': '#',
    '#.#.#': '#',
    '###.#': '#',
    '#...#': '#',
    '..#.#': '.',
    '.##..': '#',
    '.#...': '#',
    '.##.#': '#',
    '.####': '.',
    '.#.##': '.',
    '..##.': '.',
    '##.#.': '.',
    '#.##.': '.',
    '#..##': '.',
    '###..': '.',
    '....#': '.',
    '#####': '#',
    '#....': '.',
    '..#..': '#',
    }

# 360 each
big_count = 50000000000
current = init
zero = 0
patterns = {}
count = 0
old_sum = 0
old_diff = 0
for i in range(2000):
    print(i)
    zero += 2
    next = '..'
    for k in range(len(current)):
        if k < 2:
            match = '.' * (2 - k)
            match += current[0:(k + 3)]
        elif k + 2 > len(current):
            match = current[(k - 2):]
            match += '.' * (len(current) - k)
        else:
            match = current[(k - 2):(k + 3)]

        if match in data:
            next += data[match]
        else:
            next += '.'

    next += '..'

    current = next

    # p = current[(zero - 5):]
    # p = p.rstrip('.')
    # # print(p)
    # if p not in patterns:
    #     patterns[p] = {
    #             'start': i,
    #             'end': i,
    #             'cyckle': {},
    #             }
    # else:
    #     cyckle = i - patterns[p]['start']
    #     if cyckle not in patterns[p]['cyckle']:
    #         patterns[p]['cyckle'][cyckle] = 0
    #     patterns[p]['cyckle'][cyckle] += 1
    #     patterns[p]['start'] = patterns[p]['end']
    #     patterns[p]['end'] = i

    # out = False
    # for c in patterns[p]['cyckle']:
    #     print(patterns[p]['cyckle'][c] > 200, (big_count - i - 1) % c)
    #     if patterns[p]['cyckle'][c] > 200 and (big_count - i - 1) % c == 0:
    #         out = True
    # if out:
    #     break

    # print(patterns[p])
    # print('p', len(patterns))

    # sum = 0
    # for i, p in enumerate(current):
    #     if p == '#':
    #         sum += i - zero
    # print(sum)

    # sum_diff = sum - old_sum
    # if sum_diff not in patterns:
    #     patterns[sum_diff] = True
    #     count = 1
    # elif patterns[sum_diff] and sum_diff == old_diff:
    #     count += 1
    #     if 1000 < i:
    #         big_sum = (big_count - i) * sum_diff + sum
    #         print('Result:', big_sum)
    #         break

    # elif sum_diff != old_diff:
    #     patterns[old_diff] = False
    #     count = 1

    # old_diff = sum_diff
    # old_sum = sum

    # print('s', sum_diff, count)


print(current)
print(zero, len(current))
sum = 0
for i, p in enumerate(current):
    if p == '#':
        sum += i - zero

print('Result:', sum)

