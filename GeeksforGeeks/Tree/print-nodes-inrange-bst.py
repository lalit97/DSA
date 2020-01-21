def printNearNodes(root,l,h):
    if root is not None:
        if root.data > l:
            printNearNodes(root.left, l, h)
        if l <= root.data <= h:
            print(root.data, end=' ')
        if root.data < h:
            printNearNodes(root.right, l, h)
    
