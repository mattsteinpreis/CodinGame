import numpy as np

def update_box(box, pos, direction):
    x, y = pos
    xmin, xmax = box[0]
    ymin, ymax = box[1]
    if len(direction) == 1:
        direction += direction

    if direction[0] == 'U':
        ymax = y-1
    if direction[0] == 'D':
        ymin = y+1
    if direction[1] == 'L':
        xmax = x-1
    if direction[1] == 'R':
        xmin = x+1
    if direction[1] in ['U', 'D']:
        xmin = xmax = x
    if direction[0] in ['L', 'R']:
        ymin = ymax = y

    return [(xmin, xmax), (ymin, ymax)]

def center(box):
    xmin, xmax = box[0]
    ymin, ymax = box[1]
    x = int(np.mean([xmin, xmax]))
    y = int(np.mean([ymin, ymax]))
    return x, y

width, height = [int(i) for i in input().split()]
n_jumps = int(input())
x0, y0 = [int(i) for i in input().split()]

current_box = [(0, width), (0, height)]
current_pos = [x0, y0]
while True:
    bomb_dir = input()
    current_box = update_box(current_box, current_pos, bomb_dir)
    current_pos = center(current_box)
    print("{} {}".format(current_pos[0], current_pos[1]))


