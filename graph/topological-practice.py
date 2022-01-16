'''
https://www.youtube.com/watch?v=n_yl2a6n7nM
https://www.geeksforgeeks.org/topological-sorting/
https://practice.geeksforgeeks.org/problems/topological-sort/1

https://medium.com/@yasufumy/algorithm-depth-first-search-76928c065692
'''




def topoSort(n, graph):
    visited = set()
    stack = []
    # given that node are between 0 and n-1
    for node in range(n):  # now works for disconnected graphs
        if node not in visited:
            dfs_topolo(graph, node, visited, stack)
    return stack[::-1]


def dfs_topolo(graph, node, visited, stack):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs_topolo(graph, neighbour, visited, stack)
        stack.append(node)


if __name__ == '__main__':
    graph = {
        'A' : ['B','G'],
        'B' : ['C'],
        'C' : ['A','D'],
        'D' : ['E', 'F'],
        'E' : [],
        'F' : [],
        'G' : ['C']
    }
    n = 7
    ans = topoSort(n, graph)
    print(ans)