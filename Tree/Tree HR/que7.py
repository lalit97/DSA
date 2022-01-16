'''
https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/dummy3-4/
'''
class Node:
    def __init__(self, val):
        self.info = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val > current.info:
                    if current.right is None:
                        current.right = Node(val)
                        break
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = Node(val)
                        break
                    else:
                        current = current.left

    def max_ht(self, root):
        if root:
            return 1 + max(self.max_ht(root.left), self.max_ht(root.right))
        else:
            return 0


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        lis = list(map(int, input().split()))
        tree = BinarySearchTree()
        for i in lis:
            tree.create(i)
        height = tree.max_ht(tree.root)
        print(height)
