'''
https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
'''

def dfs(g,N):
    node = 0  # given 0 will be first node always
    visited = set()
    dfs_helper(visited, g, node)


def dfs_helper(visited, g, node):
    if node not in visited:
        visited.add(node)
        print(node, end=' ')
        for neighbour in g[node]:
            dfs_helper(visited, g, neighbour)
