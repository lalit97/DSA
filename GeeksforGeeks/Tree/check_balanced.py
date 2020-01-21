'''
https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1
'''



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBalanced(root):
    if root is None:
        return True
    l_height = get_height(root.left)
    r_height = get_height(root.right)
    diff = abs(l_height - r_height)
    return (diff <= 1) and isBalanced(root.left) and isBalanced(root.right)


def get_height(node):
    if node is None:
        return 0
    else:
        return 1 + max(get_height(node.left), get_height(node.right))