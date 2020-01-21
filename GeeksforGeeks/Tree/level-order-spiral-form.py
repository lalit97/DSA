from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printSpiral(root):
    if root is None:
        return

    print(root.data, end=' ')
    queue = deque()
    if root.left is not None:
        queue.append(root.left)
    if root.right is not None:
        queue.append(root.right)
    queue.append(None)

    flag = True
    while queue:
        node = queue[0]
        if node:
            if flag:
                while queue[0] is not None:
                    node = queue.popleft()
                    print(node.data, end=' ')
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
                queue.popleft()
            else:
                queue.appendleft(None)
                while queue[-1] is not None:
                    node = queue.pop()
                    print(node.data, end=' ')
                    if node.right is not None:
                        queue.appendleft(node.right)
                    if node.left is not None:
                        queue.appendleft(node.left)
            flag = not flag
        else:
            queue.popleft()


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)  
    root.right.left = Node(5) 
    root.right.right = Node(4)
    print("Spiral Order traversal of binary tree is")
    printSpiral(root)