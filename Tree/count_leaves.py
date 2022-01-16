
'''
one of the way
'''
count = 0
def countLeaves(root):
    global count
    count = 0
    count_helper(root)
    return count


def count_helper(root):
    global count
    if root is None:
        return None

    if root.left is None and root.right is None:
        count += 1

    count_helper(root.left)
    count_helper(root.right)

############################################
'''
more smarter
'''

def countLeaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None
        return 1

    return countLeaves(root.left) + countLeaves(root.right)