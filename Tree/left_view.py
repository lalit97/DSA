'''
https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
'''


from collections import deque

def LeftView(root):
    queue = deque()
    queue.append(root)
    queue.append(None)  # delimeter for this level

    while queue:
        node = queue[0]
        if node:
            print(node.data, end=' ')
            while (queue[0] != None):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            queue.append(None)  # delimeter for next level
        queue.popleft()  # removing delimeter of last level