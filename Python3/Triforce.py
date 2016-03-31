def startsize(n):
    return n * 2 - 1


def triforce(n):
    star_list = []
    max_stars = startsize(n)

    # bottom triangles
    middle_buff = 1
    left_buff = 0
    n_stars = max_stars
    for i in range(n):
        star_str = (' ' * left_buff) + \
                   ('*' * n_stars) + \
                   (' ' * middle_buff) + \
                   ('*' * n_stars)
        star_list.append(star_str)
        middle_buff += 2
        left_buff += 1
        n_stars -= 2

    # top triangle
    n_stars = max_stars
    for i in range(n):
        star_str = (' ' * left_buff) + \
                   ('*' * n_stars)
        if i == n - 1:
            star_str = '.' + star_str[1:]
        star_list.append(star_str)
        left_buff += 1
        n_stars -= 2

    return star_list


def show(l):
    for line in l[::-1]:
        print(line)


def test():
    t = triforce(1)
    show(t)

    t = triforce(2)
    show(t)

    t = triforce(10)
    show(t)


def CodinGame():
    n = int(input())
    t = triforce(n)
    show(t)


if __name__ == '__main__':
    CodinGame()
