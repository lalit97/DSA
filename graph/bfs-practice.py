


from collections import deque


def bfs(g,N):
    '''
    can use queue module already imported
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the bfs of the graph from node 0, newline is given by driver code
    '''
    # code here
    node = 0
    visited = set()
    bfs_helper(visited, g, node)


def bfs_helper(visited, graph, node):
    queue = deque()
    queue.append(node)
    visited.add(node)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
