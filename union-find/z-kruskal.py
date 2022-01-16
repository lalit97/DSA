'''
understanding -> 

https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/

implementation -> 

taking help of Graph bfs dfs implementations
union find implementations of mine 
https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

'''


from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, a, b, weight):
        self.graph[weight].append((a, b))



def root(i):
    while vertices[i] != i:
        i = vertices[i]
    return i


def find(a, b):
    return root(a) == root(b)


def union(a, b):
    root_a = root(a)
    root_b = root(b)

    if size[root_a] < size[root_b]:
        vertices[root_a] = vertices[root_b]
        size[root_b] += size[root_a]
    else:
        vertices[root_b] = vertices[root_a]
        size[root_a] += size[root_b]



def kruskal_mst(graph):
    sorted_weights = sorted(graph)
    count, result = 0, 0
    for weight in sorted_weights:
        a, b = graph[weight][0]  # first item of list
        if not find(a, b):
            count += 1
            result += weight
            union(a, b)
        if count == n - 1:  # MST is complete
            break
    return result


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1, 10) 
    g.add_edge(0, 2, 6) 
    g.add_edge(0, 3, 5) 
    g.add_edge(1, 3, 15) 
    g.add_edge(2, 3, 4) 
    graph = g.graph

    n = 4  # vertices count 
    vertices = [i for i in range(n)]
    size = [1 for i in range(n)]
    print(kruskal_mst(graph))
