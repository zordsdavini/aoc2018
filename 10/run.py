f = open('input.txt', 'r')
data = {}
for i, row in enumerate(f):
    data[i] = {
            'x': int(row[10:16].strip()),
            'y': int(row[18:24].strip()),
            'dx': int(row[36:38].strip()),
            'dy': int(row[40:42].strip()),
            }

k = 1
position = {}
for d in data:
    position[d] = {
            'x': data[d]['x'],
            'y': data[d]['y'],
            }

while True:
    k += 1
    scena = {}
    max_x = max_y = min_x = min_y = None
    x_diff = y_diff = None
    for d in data:
        x = position[d]['x'] + data[d]['dx']
        y = position[d]['y'] + data[d]['dy']
        position[d] = {
                'x': x,
                'y': y,
                }
        if x not in scena:
            scena[x] = {}
        scena[x][y] = '#'

        if max_x is None:
            max_x = min_x = x
            max_y = min_y = y
        else:
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

    new_x_diff = abs(max_x - min_x)
    new_y_diff = abs(max_y - min_y)

    # if x_diff is not None and new_x_diff > x_diff:
    #     continue

    x_diff = new_x_diff
    y_diff = new_y_diff

    if x_diff > 130:
        continue 

    print(k - 1)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if x in scena and y in scena[x]:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()
