__author__ = 'matt'

def median(l, sort=True):
    s = l
    if sort:
        s = sorted(s)
    le = len(s)
    even = le % 2 == 0
    half = int(le / 2)
    if even:
        return 0.5*(s[half] + s[half-1])
    return s[half]

def wire_length(xmin, xmax, yl, y):
    length = xmax - xmin
    for yi in yl:
        length += abs(yi - y)
    return int(length)

#count = 0
#mean_y = 0
#min_x = 2**30
#max_x = -min_x
coordinates = {}
shared = {}
n = int(raw_input())
for i in xrange(n):
    x, y = [int(j) for j in raw_input().split()]
    if coordinates.has_key(x):
        coordinates[x].append(y)
        shared[x] = coordinates[x]
    else:
        coordinates[x] = [y]


x_list = sorted(coordinates.keys())
y_list = sorted([i for j in coordinates.values() for i in j])

x_min = min(x_list)
x_max = max(x_list)

y_med = median(y_list, False)

for x in shared.keys():
    y_x = shared[x]
    if len(y_x) == 3:
        y_med = median(y_x, True)
        break
    y_med = median(y_x + [y_med])

print wire_length(x_min, x_max, y_list, y_med)