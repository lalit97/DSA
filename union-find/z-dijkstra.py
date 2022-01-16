'''
understanding 

https://www.youtube.com/watch?v=lAXZGERcDf4&t=771s

implementation using 

https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/DijkstraShortestPath.java

https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/

###############
If you like to get the shortest path data 

https://www.geeksforgeeks.org/binary-heap/

https://www.geeksforgeeks.org/dijkstras-algorithm-for-adjacency-list-representation-greedy-algo-8/


https://stackoverflow.com/questions/1465662/how-can-i-implement-decrease-key-functionality-in-pythons-heapq
answer number 4
'''

import heapq
from collections import defaultdict


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('inf') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    heapq.heapify(pq)
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


if __name__ == '__main__':

    graph = {
        'A': [('B', 5), ('D', 9), ('E', 2)],
        'B': [('A', 5), ('C', 2)],
        'C': [('B', 2), ('D', 3)],
        'D': [('A', 9), ('C', 3), ('F', 2)],
        'E': [('A', 2), ('F', 3)],
        'F': [('D', 2), ('E', 3)]
    }

    print(calculate_distances(graph, 'A'))