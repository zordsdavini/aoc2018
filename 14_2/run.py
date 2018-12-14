inpt = '077201'

i = 'i'
s = 's'
e = [
        {
            i: 0,
            s: 3
            },
        {
            i: 1,
            s: 7
            },
        ]


rcp = [3, 7]
loop = 0
while True:
    loop += 1
    sum = 0
    for k in range(2):
        sum += e[k][s]

    for j in str(sum):
        rcp.append(int(j))

    for fi in range(2):
        e[fi][i] = (e[fi][i] + 1 + e[fi][s]) % len(rcp)
        e[fi][s] = rcp[e[fi][i]]

    if loop % 500 == 0:
        print(len(rcp))
        search = ''.join(map(str, rcp[-1000:])).find(inpt)
        if search >= 0:
            search = ''.join(map(str, rcp)).find(inpt)
            print('Score:', search)
            break
