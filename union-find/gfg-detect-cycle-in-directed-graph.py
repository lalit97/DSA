'''
Resource --> 
https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
'''



'''
from collections import defaultdict

ans = 0
def dfs(vert, graph, visited, recur_call):
    global ans 

    if vert not in recur_call:
        recur_call.add(vert)
    else:
        ans = 1  # setting global answer equals to 1


    if vert not in visited:
        visited.add(vert)
        for neighbour in graph[vert]:
            dfs(neighbour, graph, visited)


def isCyclic(n, graph):
    global ans 
    ans = 0  # setting answer zero for each iteration
    visited = set()
    for vert in list(graph):  # in case graph is disconnected
        recur_call = set()
        dfs(vert, graph, visited, recur_call)  
    return ans

# if we would have called dfs from __main__ we can call like dfs(vert) only 
# and it could have accessed graph, visited on itself 
# but here we have to pass everything 


if __name__ == '__main__':
    graph = defaultdict(list)
    graph[0].append(1)
    graph[0].append(0)
    print(graph)
    print(isCyclic(3, graph))


'''




from collections import defaultdict

ans = None

def dfs(vert, graph, visited, recur_call):
    global ans 
    visited.add(vert)
    recur_call.add(vert)
    for neighbour in graph[vert]:
        if  neighbour not in visited:
            dfs(neighbour, graph, visited, recur_call)
        elif neighbour in recur_call:
            ans = 1
    recur_call.remove(vert)


def isCyclic(n, graph):
    global ans
    ans = 0
    visited = set()
    recur_call = set()
    for vert in list(graph):
        if vert not in visited:
            dfs(vert, graph, visited, recur_call)  
    return ans



if __name__ == '__main__':
    graph = defaultdict(list)
    graph[0].append(1)
    graph[0].append(0)
    print(graph)
    print(isCyclic(3, graph))
