'''
Topological sort function

https://www.youtube.com/watch?v=n_yl2a6n7nM
https://www.geeksforgeeks.org/topological-sorting/

'''
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, a, b):
        self.graph[a].append(b)


def dfs_topolo(graph, node):
    if node not in visited:
        visited.add(node)
        print(node, end=' ')  # to get dfs
        for neighbour in graph[node]:
            dfs_topolo(graph, neighbour)
        stack.append(node)


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B') 
    g.add_edge('A', 'C') 
    g.add_edge('B', 'D') 
    g.add_edge('B', 'E') 
    g.add_edge('C', 'F') 
    g.add_edge('E', 'F')


    visited = set()
    stack = []
    graph = g.graph
    print('DFS OF GRAPH')
    dfs_topolo(graph, 'A')
    print()
    print('TOPOLOGICAL SORT')
    while stack:
        item = stack.pop()
        print(item, end=' ')
    print()