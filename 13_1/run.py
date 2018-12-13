import sys

print('Preparing map...')

f = open('input.txt', 'r')

# test = """/->-\\        
# |   |  /----\\
# | /-+--+-\\  |
# | | |  | v  |
# \\-+-/  \\-+--/
#   \\------/   """

# f = test.split('\n')
# print(f)

cart = {}
car_m = {}
car_cs = {
        '<': '-',
        '>': '-',
        '^': '|',
        'v': '|',
        } 

p_rules = {
        '>-': (0, 1, '>'),
        '>\\': (1, 0, 'v'),
        '>/': (-1, 0, '^'),
        '<-': (0, -1, '<'),
        '</': (1, 0, 'v'),
        '<\\': (-1, 0, '^'),
        '^|': (-1, 0, '^'),
        '^/': (0, 1, '>'),
        '^\\': (0, -1, '<'),
        'v|': (1, 0, 'v'),
        'v/': (0, -1, '<'),
        'v\\': (0, 1, '>'),
        }

turns = {
        1: {    # left
            '>': ('^', '|'),
            '^': ('<', '-'),
            '<': ('v', '|'),
            'v': ('>', '-'),
        },
        2: {    # stright
            '>': ('>', '-'),
            '^': ('^', '|'),
            '<': ('<', '-'),
            'v': ('v', '|'),
        },
        3: {    # right
            '>': ('v', '|'),
            '^': ('>', '-'),
            '<': ('^', '|'),
            'v': ('<', '-'),
        },
        }

for x, row in enumerate(f):
    row = row.strip('\t\n\r')
    if x not in cart:
        cart[x] = {}

    for y, c in enumerate(row):
        car = False
        if c in car_cs:
            car = True

            if x not in car_m:
                car_m[x] = {}
            car_m[x][y] = {
                    'c': c,
                    'turn': 1,
                    }

            c = car_cs[c]

        cart[x][y] = {
                'car': car,
                'c': c,
                }


def move(x, y):
    car = car_m[x][y]
    car_c = car['c']

    road = cart[x][y]
    road_c = road['c']
    if road_c == '+':
        t = car['turn']
        n_t = turns[t][car_c]
        car_c = n_t[0]
        road_c = n_t[1]

        t += 1
        if t > 3:
            t = 1

        car['turn'] = t

    n_p = p_rules[car_c + road_c]
    n_x = x + n_p[0]
    n_y = y + n_p[1]
    car['c'] = n_p[2]

    if cart[n_x][n_y]['car']:
        cart[x][y]['car'] = False
        # cart[n_x][n_y]['c'] = 'X'
        return [True, n_x, n_y, None]

    cart[n_x][n_y]['car'] = True
    cart[x][y]['car'] = False

    return [False, n_x, n_y, car]


print('Moving...')
tick = 0
while True:
    tick += 1
    new_car_m = {}
    for x in sorted(car_m.keys()):
        for y in sorted(car_m[x].keys()):
            p = move(x, y)
            if p[0]:
                # for x in cart:
                #     print(x, end=' ')
                #     for y in cart[x]:
                #         print(cart[x][y]['c'], end='')
                #     print()

                print('Crash (%s): %i,%i' % (tick, p[2], p[1]))
                sys.exit()

            if p[1] not in new_car_m:
                new_car_m[p[1]] = {}
            new_car_m[p[1]][p[2]] = p[3]

    car_m = new_car_m
