'''
https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-cursed-tree/
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
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break

    def get_lca(self, current, a, b):
        info = current.info 
        if info > a and info > b:
            return self.get_lca(current.left, a, b)
        elif info < a and info < b:
            return self.get_lca(current.right, a, b)
        else:
            return current

    def search(self, current, val):
        maxi = 0
        while True:
            if current.info > maxi:
                maxi = current.info
            if current.info == val:
                return maxi
            elif current.info > val:
                current = current.left
            else:
                current = current.right 


if __name__ == '__main__':
    n = int(input())
    lis = list(map(int, input().split()))
    a,b = map(int, input().split())
    tree = BinarySearchTree()
    for i in lis:
        tree.create(i)
    local_parent = tree.get_lca(tree.root, a, b)
    max_a = tree.search(local_parent, a)
    max_b = tree.search(local_parent, b) 
    print(max(max_a, max_b))
