__author__ = 'matt'


class Bender:
    def __init__(self, bender_map):
        self.bendermap = bender_map
        self.r, self.c = bender_map.get_start()
        self.direction = 'S'
        self.next_r = self.r+1
        self.next_c = self.c
        self.breaker = False
        self.inverted = False
        self.current_tile = '@'
        self.moves = []
        self.teleport = False

    def position(self):
        return self.r, self.c

    def invert(self):
        self.inverted = not self.inverted

    def toggle_breaker(self):
        self.breaker = not self.breaker

    def breaker(self):
        return self.toggle_breaker()

    def force_direction(self, direction):
        self.direction = direction

    def set_next_direction(self, n):
        directions = ['S', 'E', 'N', 'W']
        if self.inverted:
            directions = directions[::-1]
        self.direction = directions[n]

    def set_next_position(self):
        turn_counter = 0
        while True:
            r, c = self.r, self.c
            if self.direction == 'S':
                r += 1
            elif self.direction == 'N':
                r -= 1
            elif self.direction == 'E':
                c += 1
            else:
                c -= 1
            nt = self.tile(r, c)  # next tile
            if nt == '#' or (nt == 'X' and not self.breaker):
                self.set_next_direction(turn_counter)
                turn_counter += 1
            else:
                if nt == 'X':
                    self.bendermap.break_obstacle(r, c)
                self.next_r, self.next_c = r, c
                return

    def move(self):
        movement = self.movement()
        if not self.teleport:
            self.moves.append(movement)
        self.r = self.next_r
        self.c = self.next_c
        self.update()

    def movement(self):
        d = self.direction
        if d == 'S':
            return 'SOUTH'
        elif d == 'W':
            return 'WEST'
        elif d == 'E':
            return 'EAST'
        else:
            return 'NORTH'

    def update(self):
        self.current_tile = self.bendermap.location(self.r, self.c)
        t = self.current_tile
        if t == 'I':
            self.invert()
        if t == 'B':
            self.toggle_breaker()
        if t in ['S', 'W', 'E', 'N']:
            self.force_direction(t)

        if t == 'T':
            self.teleport = not self.teleport
            if self.teleport:
                self.next_r, self.next_c = self.bendermap.transporters[(self.r, self.c)]
            else:
                self.set_next_position()
        else:
            self.set_next_position()

    def set_location(self, r, c):
        self.r = r
        self.c = c

    def tile(self, r=-1, c=-1):
        if r < 0:
            r = self.r
            c = self.c
        return self.bendermap.location(r, c)

    def traverse_map(self, print_path=True, stepwise = False, max_steps = 1000000):
        count = 0
        while count < max_steps:
            if stepwise:
                _ = raw_input()
            self.move()
            if print_path:
                #lprint count, self.moves[-1], self.tile()
                print self.summary()
            count += 1
            if self.tile() == '$':
                return 'FINISHED'
        return 'LOOP'

    def summary(self):
        print 'Position:', self.position()
        print 'Tile:', self.current_tile
        print 'Direction:', self.direction
        print (self.r, self.c)



class BenderMap:
    def __init__(self):
        self.map = []
        self.start = (None, None)
        self.transporters = {}

    def fill_row(self, row_str):
        row_list = [ch for ch in row_str]
        self.map.append(row_list)

    def location(self, r, c):
        return self.map[r][c]

    def break_obstacle(self, r, c):
        self.map[r][c] = ' '

    def print_map(self):
        for irow in range(len(self.map)):
            self.print_row(irow)

    def print_row(self, r):
        print ''.join(self.map[r])

    def find_start(self):
        for i, r in enumerate(self.map):
            for j, c in enumerate(r):
                if c == '@':
                    self.start = (i, j)
                    return

    def get_start(self):
        self.find_start()
        return self.start

    def find_transporters(self):
        t1 = None
        for i, r in enumerate(self.map):
            for j, c in enumerate(r):
                if c == 'T':
                    t = (i, j)
                    if t1:
                        self.transporters[t1] = t
                        self.transporters[t] = t1
                        return
                    else:
                        t1 = t


# the_map = BenderMap()
# n_rows, n_cols = [int(i) for i in raw_input().split()]
# for i in xrange(n_rows):
#    row = raw_input()
#    the_map.fill_row(row)


# Testing
m = BenderMap()
#m.fill_row('#####')
#m.fill_row('# $ #')
#m.fill_row('#  @#')
#m.fill_row('#####')
m.fill_row('##########')
m.fill_row('#    T   #')
m.fill_row('#        #')
m.fill_row('#        #')
m.fill_row('#        #')
m.fill_row('#@       #')
m.fill_row('#        #')
m.fill_row('#        #')
m.fill_row('#    T  $#')
m.fill_row('##########')

m.find_start()
m.find_transporters()

robot = Bender(m)
robot.update()
#robot.summary()
#robot.move()
#robot.summary()



run = robot.traverse_map(print_path=False, stepwise=False)
# print run
# print
# print 'MOVES:'
for move in robot.moves:
    print move
