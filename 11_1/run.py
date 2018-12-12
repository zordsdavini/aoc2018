class Grid:
    grid = {}
    serial = None

    def __init__(self, serial):
        self.serial = serial
        self.grid_power()

    def grid_power(self):
        for x in range(1, 301):
            for y in range(1, 301):
                rack_id = x + 10
                power = rack_id * y + self.serial
                power *= rack_id
                power = power % 1000 // 100
                power -= 5

                if x not in self.grid:
                    self.grid[x] = {}
                self.grid[x][y] = power

    def get_power(self, x, y):
        return self.grid[x][y]


print('TEST...')
t = Grid(8)
print('in 3,5:', t.get_power(3, 5) == 4)
t = Grid(57)
print('in 122,79:', t.get_power(122, 79) == -5)
t = Grid(39)
print('in 217,196:', t.get_power(217, 196) == 0)
t = Grid(71)
print('in 101,153:', t.get_power(101, 153) == 4)

print('\nCalculating power blocks...')
grid = Grid(5177)

pgrid = {}
for x in range(1, 299):
    for y in range(1, 299):
        power = 0
        for i in range(3):
            for j in range(3):
                power += grid.get_power(x + i, y + j)

        if x not in pgrid:
            pgrid[x] = {}
        pgrid[x][y] = power

maximum = -20
max_x = None
max_y = None
for x in pgrid:
    for y in pgrid[x]:
        value = pgrid[x][y]
        if value > maximum:
            maximum = value
            max_x = x
            max_y = y

print('Result:', max_x, max_y)
