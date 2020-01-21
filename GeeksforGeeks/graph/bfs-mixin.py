'''
mixed version of code from 
https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/and 
https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
'''
from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, a, b):
        self.graph[a].append(b)


visited = set()
queue = deque()

def bfs(visited, graph, node):
    visited.add(node)
    queue.append(node)
    while queue:
        node = queue.popleft() 
        print (node, end=' ') 
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1) 
    g.add_edge(0, 2) 
    g.add_edge(1, 2) 
    g.add_edge(2, 0) 
    g.add_edge(2, 3) 
    g.add_edge(3, 3)
    graph = g.graph
    bfs(visited, graph, 2)
