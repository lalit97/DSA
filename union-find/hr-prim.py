'''
https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/

This one is working fully got submitted.

hackerearth Test Cases gives only one way of data for a undirected graph
1 2 7
1 4 6
4 2 9
4 3 8
2 3 6

like if 1 2 7 is mentioned, 
they do not mention 2 1 7

so we run the function twice
    graph.add_edge(a, b, w)
    graph.add_edge(b, a, w)
'''


import heapq
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, a, b, weight):
        self.graph[a].append((b, weight))


def prim_mst(start):
    result = 0
    visited = set([start])

    edges = [(weight, start, to) for to, weight in graph[start]]
    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            result += weight
            for to_next, weight in graph[to]:
                if to_next not in visited:
                    heapq.heappush(edges, (weight, to, to_next))
    return result


if __name__ == '__main__':
    graph = Graph()
    n, m = map(int, input().split())
    for i in range(m):
        a, b, w = map(int, input().split())
        graph.add_edge(a, b, w)
        graph.add_edge(b, a, w)
    graph = graph.graph
    print(prim_mst(1))