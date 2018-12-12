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
                
    def get_additional(self, x, y, size):
        value = 0
        for i in range(x, x + size):
            value += self.grid[i][y + size - 1]
        for i in range(y, y + size - 1):
            value += self.grid[x + size - 1][i]

        return value


def get_biggest_div(k):
    for i in range(k - 1, 1, -1):
        if k % i == 0:
            return i
    return 0


print('Calculating power blocks...')
grid = Grid(5177)

maximum = -20
max_x = None
max_y = None
max_size = 1
for x in grid.grid:
    for y in grid.grid[x]:
        power = grid.grid[x][y]
        if power > maximum:
            maximum = power
            max_x = x
            max_y = y

pgrid = {1: grid.grid}
for size in range(2, 301):
    # biggest_div = get_biggest_div(size)
    # if biggest_div != 0:
    #     dgrid = pgrid[biggest_div]
    #     sdiv = size // biggest_div
    # else:
    #     dgrid = pgrid[size - 1]
    #     sdiv = None

    dgrid = pgrid[size - 1]
    # print(size, biggest_div, len(grid.grid) + 1 - size)
    print(size)
    for x in range(1, len(grid.grid) + 1 - size):
        for y in range(1, len(grid.grid) + 1 - size):
            # if sdiv is not None:
            #     power = 0
            #     for i in range(sdiv):
            #         for j in range(sdiv):
            #             power += dgrid[x + i * sdiv][y + j * sdiv]
            # else:
            power = dgrid[x][y] + grid.get_additional(x, y, size)

            if size not in pgrid:
                pgrid[size] = {}
            if x not in pgrid[size]:
                pgrid[size][x] = {}
            pgrid[size][x][y] = power
            if power > maximum:
                maximum = power
                max_x = x
                max_y = y
                max_size = size

print('Result:', max_x, max_y, max_size)
