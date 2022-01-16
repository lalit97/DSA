'''
https://practice.geeksforgeeks.org/problems/symmetric-tree/1
'''


def is_mirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None:
        return root1.val == root2.val and is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)
    else:
        return False


def isSymmetric(root):
    if is_mirror(root.left, root.right):
        return True
    return False