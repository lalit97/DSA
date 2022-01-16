'''
https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/
'''

'''
we are taking weights as keys just for simplicity 
we can find edges and vertices and all if the given structure is different
all we need is understanding of the algorithm.
'''

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, a, b, weight):
        self.graph[weight].append((a, b))


# start of Union Find 
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
# End of Union-Find 


def kruskal_mst(graph):
    sorted_weights = sorted(graph)
    count, result = 0, 0
    for weight in sorted_weights:
        for ver1, ver2 in graph[weight]:
            if not find(ver1, ver2):
                count += 1
                result += weight
                union(ver1, ver2)
            if count == n - 1:  # MST is complete
                break
    return result


if __name__ == '__main__':
    graph = Graph()
    n, m = map(int, input().split())
    for i in range(m):
        a, b, w = map(int, input().split())
        graph.add_edge(a, b, w)
    graph = graph.graph


    # given that the vertices will be from 1 to n
    vertices, size = dict(), dict()
    for i in range(1, n+1):
        vertices[i] = i
        size[i] = 1
    print(kruskal_mst(graph))
