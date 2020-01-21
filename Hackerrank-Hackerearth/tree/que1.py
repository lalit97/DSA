'''
https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/practice-problems/algorithm/mirror-image-2/description/

https://www.hackerearth.com/submission/27600152/
'''
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.info)


class BinaryTree:
    def __init__(self):
        self.root = None

    # def create(self, parent, child, pos):
    #     if pos == 'L':
    #         current.left = Node(child)



if __name__ == '__main__':
#    n,q = map(int, input().split())
    tree = BinaryTree()
    tree.root = Node(1)
    if tree.root == 1:
        print('han hai')

    # for _ in range(n-1):
    #     parent, child, pos = map(int, input().split())
    #     tree.create(parent, child, pos)


    # for i in range(q):
    #     node = int(input())

