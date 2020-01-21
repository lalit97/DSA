'''
https://practice.geeksforgeeks.org/problems/add-all-greater-values-to-every-node-in-a-bst/1
'''


'''
doing sum in a recursive code

use global variables
do not pass global variables as parameters of function

write them out of the functions

then if there are multiple test cases
just make it zero in the main function (here modifyBST)
'''

sum_ = 0

def modifyBST(root):
    global sum_
    sum_ = 0
    rev_inorder(root)


def rev_inorder(root):
    global sum_
    if root is None:
        return None
    rev_inorder(root.right)
    root.data = root.data + sum_
    sum_ = root.data
    rev_inorder(root.left)