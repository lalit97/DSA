'''
https://practice.geeksforgeeks.org/problems/array-to-bst/0
'''

low = 0, high = n-1
from math import floor


def array_to_bst(lis, low, high):
    if low > high:
        return None

    mid = low + f((high - low)/2)
    root = Node(lis[mid])
    root.left = array_to_bst(lis, low, mid -1 )
    root.right = array_to_bst(lis, mid+1, high)

    return root
