import string

f = open('input.txt', 'r')
from_l = {}
to_l = {}
for row in f:
    row = row.strip('\t\n\r')
    p = row.split()
    if p[1] not in from_l:
        from_l[p[1]] = []
    if p[7] not in to_l:
        to_l[p[7]] = []
    from_l[p[1]].append(p[7])
    to_l[p[7]].append(p[1])

start_set = set(from_l.keys()) - set(to_l.keys())
start = []
while len(start_set):
    start.append(start_set.pop())
start.sort()
waiting = start[::-1]

result = ''
while len(waiting):
    not_added = True
    back = []
    while not_added:
        f = waiting.pop()
        if f in to_l:
            all = True
            for h in to_l[f]:
                if h not in result:
                    all = False
            if not all:
                back.append(f)
                continue

        result += f
        not_added = False

    waiting += back

    if f in from_l:
        cc = from_l[f]
        for c in cc:
            if c not in waiting and c not in result:
                waiting.append(c)

    waiting.sort()
    waiting.reverse()

print('Result:', result)
