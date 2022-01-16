'''
https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/
https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/

implementation -> 

https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/

'''

import heapq
from collections import defaultdict



def prim_mst(graph, start):
    count = 0
    visited = set([start])

    edges = [(weight, start, to) for to, weight in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            count += weight
            for to_next, weight in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (weight, to, to_next))

    return count



if __name__ == '__main__':
    graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 8, 'E': 4},
        'C': {'A': 3, 'B': 1, 'F': 5},
        'D': {'B': 8, 'E': 7},
        'E': {'B': 4, 'D': 7, 'F': 9},
        'F': {'C': 5, 'E': 9, 'G': 10},
        'G': {'F': 10},
    }

    print(prim_mst(graph, 'A'))

'''
to make something like this with custom inputs
graph = defaultdict(dict)

In [15]: for i in range(5):
    ...:     a, b, w = map(int, input().split())
    ...:     d = graph[a]
    ...:     d[b] = w
    ...:
    ...:
1 2 7
1 4 6
4 2 9
4 3 8
2 3 6

In [16]: graph
Out[16]: defaultdict(dict, {1: {4: 6, 2: 7}, 4: {3: 8, 2: 9}, 2: {3: 6}})
'''