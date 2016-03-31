def rotate(grid, n=1):
    for i in range(n):
        grid = list(zip(*grid[::-1]))
    return grid


def move(grid):
    grid = rotate(grid, 3)
    n = len(grid[0])
    new_grid = []
    for row in grid:
        n_snow = row.count('#')
        n_dot = n - n_snow
        new_grid.append(['.'] * n_dot + ['#'] * n_snow)
    return rotate(new_grid)


def show(grid):
    for row in grid:
        print(''.join(row))


def codin_game():
    width, height = [int(i) for i in input().split()]
    g = []
    for i in range(height):
        line = input()
        g.append([ch for ch in line])
    g = move(g)
    show(g)

if __name__ == "__main__":
    codin_game()