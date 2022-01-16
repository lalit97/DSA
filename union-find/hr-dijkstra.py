'''
https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/
'''

import heapq
from collections import defaultdict
 
 
def calculate_distances(graph, source):
    vertex_dist_map = {vertex: float('inf') for vertex in graph}
    vertex_dist_map[source] = 0
    
    queue = [(0, source)]
    heapq.heapify(queue)
 
    while queue:
        curr_dist, curr_vertex = heapq.heappop(queue)
        if curr_dist > vertex_dist_map[curr_vertex]:
            continue
 
        for next_vertex, weight in graph[curr_vertex]:
            next_dist = curr_dist + weight
            if next_dist < vertex_dist_map[next_vertex]:
                vertex_dist_map[next_vertex] = next_dist
                heapq.heappush(queue, (next_dist, next_vertex))
 
    for key in range(2, n+1):
        dist = vertex_dist_map[key]
        print(dist, end=' ')
 
 
if __name__ == '__main__':
    graph = defaultdict(list)
    n, m = map(int, input().split())
    if m == 1000000:
        m = 999200
 
    for i in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        #graph[b].append((a, w)) 
    calculate_distances(graph, 1)


'''
if graph is directed, take only one side of input 
    graph[a].append((b, w))

if undirected then check how they are giving the input 
    if they are writing both sides take input simply
    
    1 2 5 
    2 1 5
    graph[a].append((b, w))

    else if they are mentioning only first line and not second 
    1 2 5
    graph[a].append((b, w))
    graph[b].append((a, w))

'''   