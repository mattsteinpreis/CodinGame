__author__ = 'matt'

# written for Python3

n = int(input())
stocks = [int(i) for i in input().split()]

left = 0
right = 1
max_drop = 0
while right < n:
    sr = stocks[right]
    sl = stocks[left]
    drop = sr-sl
    #print(left, right, drop)
    max_drop = min(max_drop, drop)
    if sr > sl:
        left = right
    right += 1
max_drop = min(max_drop, 0)
print(max_drop)
