'''
mixed version of code from 
https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
and 
https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

'''
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, a, b):
        self.graph[a].append(b)


visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        print(node, end=' ')
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1) 
    g.add_edge(0, 2) 
    g.add_edge(1, 2) 
    g.add_edge(2, 0) 
    g.add_edge(2, 3) 
    g.add_edge(3, 3)
    graph = g.graph
    dfs(visited, graph, 2)
