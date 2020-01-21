'''
https://practice.geeksforgeeks.org/problems/children-sum-parent/1
'''

def isSumProperty(root):
    ans = isSumProperty_helper(root)
    return 1 if ans else 0


def isSumProperty_helper(root):
    if root is None:  # case of empty tree
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        condition = root.data == root.left.data + root.right.data

    elif root.left is not None:
        condition = root.data == root.left.data

    else:
        condition = root.data == root.right.data

    return condition and isSumProperty_helper(root.left) and isSumProperty_helper(root.right)