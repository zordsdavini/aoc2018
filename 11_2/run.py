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


print('Calculating power blocks...')
grid = Grid(5177)

pgrid = {}
for size in range(1, 301):
    for x in range(1, 301 - size):
        for y in range(1, 301 - size):
            power = 0
            for i in range(size):
                for j in range(size):
                    power += grid.get_power(x + i, y + j)

            if size not in pgrid:
                pgrid[size] = {}
                if x not in pgrid[size]:
                    pgrid[size][x] = {}
                pgrid[size][x][y] = power

maximum = -20
max_x = None
max_y = None
max_size = None
for size in pgrid:
    for x in pgrid[size]:
        for y in pgrid[size][x]:
            value = pgrid[size][x][y]
            if value > maximum:
                maximum = value
                max_x = x
                max_y = y
                max_size = size

print('Result:', max_x, max_y, 301 - max_size)
