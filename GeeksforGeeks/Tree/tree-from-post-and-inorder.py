'''
https://practice.geeksforgeeks.org/problems/tree-from-postorder-and-inorder/1
'''


def buildTree(In, post, n):
    root = post[-1]
    low = 0
    high = n-1
