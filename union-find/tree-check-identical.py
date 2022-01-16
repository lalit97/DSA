'''

https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1

gfg code is better to understand
https://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/
'''



def isIdentical(root1, root2):
    if root1 is not None and root2 is not None:
        if root1.data != root2.data:
            return False
        return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
    elif root1 is None and root2 is None:
        return True 
    return False
