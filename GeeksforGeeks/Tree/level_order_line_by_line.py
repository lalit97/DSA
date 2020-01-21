
'''
https://practice.geeksforgeeks.org/problems/level-order-traversal-line-by-line/1
'''


from collections import deque

def levelOrder(root):
    queue = deque()
    queue.append(root)
    queue.append('$')

    while queue:
        node = queue[0]
        if node:
            while queue[0] != '$':
                node = queue.popleft()
                print(node.data, end=' ')
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            queue.append('$')
        queue.popleft()
        if queue:
            print('$', end=' ')
