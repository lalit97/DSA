"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


class Node:
    def __init__(self, info):
        self.info = info      #  type --> integer
        self.left = None      #  type --> Node
        self.right = None     #  type --> Node 
        self.level = None

    def __str__(self):
        info = str(self.info)
        left = str(self.left)
        right = str(self.right)
        string = 'info -> {}\nleft-> {}\nright -> {}\n'.format(info, left, right)
        return string


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root, end=' ')
        in_order(root.right)


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())
    arr = list(map(int, input().split()))
    for i in range(t):
        tree.create(arr[i])
#    in_order(tree.root)
    root = tree.root
    print(root)
    print(root.left)
    print(root.right)
