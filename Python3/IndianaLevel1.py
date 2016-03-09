__author__ = 'matt'

PATHS = {(1, 'T'): 'D',
         (1, 'L'): 'D',
         (1, 'R'): 'D',
         (2, 'L'): 'R',
         (2, 'R'): 'L',
         (3, 'T'): 'D',
         (4, 'T'): 'L',
         (4, 'R'): 'D',
         (5, 'T'): 'R',
         (5, 'L'): 'D',
         (6, 'L'): 'R',
         (6, 'R'): 'L',
         (7, 'T'): 'D',
         (7, 'R'): 'D',
         (8, 'L'): 'D',
         (8, 'R'): 'D',
         (9, 'T'): 'D',
         (9, 'L'): 'D',
         (10, 'T'): 'L',
         (11, 'T'): 'R',
         (12, 'R'): 'D',
         (13, 'L'): 'D',
         }


def next_position(x, y, t, d):
    ndir = PATHS[(t, d)]
    if ndir == 'D':
        y += 1
    elif ndir == 'L':
        x -= 1
    else:
        x += 1
    return x, y


# get maze
width, height = [int(i) for i in input().split()]
matrix = []
for line in range(height):
    matrix.append([int(i) for i in input().split()])

ex = int(input())  # unused for level 1

while True:
    input_line = input().split()
    xi = int(input_line[0])
    yi = int(input_line[1])
    direction = input_line[2][0]
    tile = matrix[yi][xi]
    xn, yn = next_position(xi, yi, tile, direction)
    print(xn, yn)
