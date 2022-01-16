'''
TAG --> BST Search implementation

https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-his-friends/
'''

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):  
        if self.root == None:
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

    def search(self, val):
        if self.root.info == val:
            return True
        else:
            current = self.root
            if val < current.info:
                return self.search_(current.left, val)
            else:
                return self.search_(current.right, val)

    def search_(self, current, val):
        if current:
            if current.info == val:
                return True
            elif current.left and val <= current.info:
                return self.search_(current.left, val)
            elif current.right and val >= current.info:
                return self.search_(current.right, val)
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    for i in range(int(input())):
        tree = BinarySearchTree()
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        st_tree = arr[:n]
        af_tree = arr[n:]
        for i in st_tree:
            tree.create(i)
        for j in af_tree:
            res = tree.search(j)
            if res:
                print('YES')  
            else:
                print('NO')
                tree.create(j)
