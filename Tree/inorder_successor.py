'''
https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1
'''

'''
remember we are asked to return to successor Node
not Node.data
'''

def inorderSuccessor(root, node):
    if node.right is not None:
        return min_right_subtree(node.right)

    return bst_search(root, node)




def min_right_subtree(node):
    if node.left is None:
        return node
    return min_right_subtree(node.left)


def bst_search(root, node):
    succ = Node(-1)
    while root is not None:
        if root.data > node.data:
            succ = root
            root = root.left
        elif root.data < node.data:
            root = root.right
        else:
            break
    return succ


###########################################
'''
Because of the some problem in gfg editor
they didn't passed the value of the new Node
so the above can not refer root.right 

so we have used this code instead
'''

def inorderSuccessor(root, n): 
    succ = None
    while root:
        if root.data > n.data:
            succ = root
            root = root.left
        elif root.data < n.data:
            root = root.right
        elif root.data == n.data and root.right:
            return leftMostChild(root.right)
        else:
            break
    return succ
  
def leftMostChild(node): 
    if not node:
        return None
        
    while node.left:
        node = node.left 
    return node