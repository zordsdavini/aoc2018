inpt = 77201

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
while True:
    print(len(rcp))
    sum = 0
    for k in range(2):
        sum += e[k][s]

    for j in str(sum):
        rcp.append(int(j))

    for fi in range(2):
        e[fi][i] = (e[fi][i] + 1 + e[fi][s]) % len(rcp)
        e[fi][s] = rcp[e[fi][i]]

    if len(rcp) > inpt + 10:
        print('Score:', ''.join(map(str, rcp))[inpt:(inpt + 10)])
        break
