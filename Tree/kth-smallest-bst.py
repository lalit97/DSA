






def k_smallest_element(root, n):
    stack = []
    while True:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        n -= 1
        if n == 0:
            return root.data
        root = root.right