'''
https://practice.geeksforgeeks.org/problems/level-order-traversal/1
'''
from collections import deque

def levelOrder(root):
    queue = deque()
    queue.append(root)

    while queue:
        item = queue.popleft()
        if item.left is not None:
            queue.append(item.left)
        if item.right is not None:
            queue.append(item.right)
        print(item.data, end=' ')