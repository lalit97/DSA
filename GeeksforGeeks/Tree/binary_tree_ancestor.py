
'''
https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1

https://www.youtube.com/watch?v=13m9ZCB8gjw&list=PLrmLmBdmIlpv_jNDXtJGYTPNQ2L1gdHxu&index=17
'''


def lca(root, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)

    if left is None and right is None:
        return None

    if left is not None and right is not None:
        return root

    return left if left is not None else right