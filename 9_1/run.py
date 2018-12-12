"""
Both parts in one
"""
# 427 players; last marble is worth 70723 points

players = {}
marbles = [0, 1]
current = 1
player = 2
limit = 7072301   
# limit = 70724    <-- for 1st part

for m in range(2, limit):
    print(m)
    next = current + 2
    if next > len(marbles):
        next = next - len(marbles)

    if m % 23 == 0:
        if player not in players:
            players[player] = 0
        players[player] += m

        next -= 9
        if next < 0:
            next += len(marbles)

        players[player] += marbles.pop(next)

    else:
        marbles.insert(next, m)

    current = next

    player += 1
    if player > 427:
        player = 1

score = 0
for p in players:
    if players[p] > score:
        score = players[p]

print('Result:', score)
