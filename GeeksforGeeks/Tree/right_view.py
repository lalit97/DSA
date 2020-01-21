

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rightView(root):
    queue = deque()
    queue.append(root)
    queue.append(None)
    while queue:
        node = queue[0]
        if node:
            while queue[0] is not None:
                node = queue[0]
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                if queue[1] is None:
                    print(node.data, end=' ')
                queue.popleft()
            queue.append(None)
        queue.popleft()


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    rightView(root)
    # inorder(root)