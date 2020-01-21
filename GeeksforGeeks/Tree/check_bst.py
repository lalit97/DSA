'''
https://practice.geeksforgeeks.org/problems/check-for-bst/1
'''

def isBST(root):
    '''
    min, max taken according to given constraints in question
    '''
    min_, max_ = 0, 1000
    return check_bst(root, min_, max_)


def check_bst(root, min_, max_):
    if root is None:
        return True

    if root.data < min_ or root.data > max_:
        return False

    return check_bst(root.left, min_, root.data) and check_bst(root.right, root.data, max_)



'''
although this is correct but upper one is faster.

def check_bst(root, min_, max_):
    if root is None:
        return True

    condition1 = min_ <= root.data <= max_
    condition2 = check_bst(root.left, min_, root.data-1)
    condition3 = check_bst(root.right, root.data+1, max_)

    return condition1 and condition2 and condition3
'''