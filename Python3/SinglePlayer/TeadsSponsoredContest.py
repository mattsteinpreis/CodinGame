__author__ = 'matt'

import collections

### NEED TO MEMOIZE

n_edges = int(input())
edges = collections.defaultdict(list)
for i in range(n_edges):
    xi, yi = [int(j) for j in input().split()]
    edges[xi].append(yi)
    edges[yi].append(xi)

all_times = []
for start_node in edges.keys():
    current_nodes = [start_node]
    hours = 0
    used = collections.defaultdict(int)
    while current_nodes:
        next_nodes = []
        for node in current_nodes:
            used[node] += 1
            for edge in edges[node]:
                if edge not in used:
                    next_nodes.append(edge)
        current_nodes = next_nodes
        if current_nodes:
            hours += 1
    all_times.append(hours)

print(min(all_times))