'''
https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
'''




from collections import defaultdict


ans = None

def dfs(vert, graph, visited, parent):
    global ans 
    visited.add(vert)
    for neighbour in graph[vert]:
        if  neighbour not in visited:
            dfs(neighbour, graph, visited, vert)
        elif neighbour != parent:
            ans = 1


def isCyclic(n, graph):
    global ans
    ans = 0
    visited = set()
    for vert in list(graph):
        if vert not in visited:
            dfs(vert, graph, visited, -1)  
    return ans


if __name__ == '__main__':
    graph = defaultdict(list)
    graph[0].append(1)
    graph[1].append(0)
    print(isCyclic(0, graph))
