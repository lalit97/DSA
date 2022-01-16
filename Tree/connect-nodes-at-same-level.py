'''
https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1
'''

'''
idea get level by level into an array and then connect
and then connect them 
'''

from collections import deque
def connect(root):
    '''
    :param root: root of the given tree
    :return: none, just connect accordingly.
    {
        # Node Class:
        class Node:
            def __init__(self,val):
                self.data = val
                self.left = None
                self.right = None
                self.nextRight = None
    }
    '''
    if root is None:
        return

    queue = deque()
    queue.append(root)
    queue.append(None)

    array = []
    array.append(root)
    array.append(None)
    while queue:
        node = queue[0]
        if node:
            while queue[0] is not None:
                node = queue.popleft()
                array.append(node)
                if node.left is not None:
                    queue.append(node.left)
                    array.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                    array.append(node.right)
            queue.append(None)
            array.append(None)
        queue.popleft()

    for index, value in enumerate(array):
        if array[i] is not None and array[i+1] is not None:
            array[i].nextRight = array[i+1]
