


def mirror(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return root

    left_tree = mirror(root.left)
    right_tree = mirror(root.right)
    root.left = right_tree
    root.right = left_tree
    return root