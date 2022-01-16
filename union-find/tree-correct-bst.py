'''
https://practice.geeksforgeeks.org/problems/fixed-two-nodes-of-a-bst/1/?track=md-tree&batchId=144
'''
'''
2 values are incorrect in bst swap them and return the root
'''


def is_bst(root, parents, min_, max_):
    if root is None:
        return True 

    condition1 = min_ <= root.data <= max_
    condition2 = is_bst(root.left, parents, min_, root.data-1)
    condition3 = is_bst(root.right, parents, root.data+1, max_)


    if not condition1:
        parents.append(root)
    if not condition2:
        parents.extend(root.left)
    if not condition3:
        parents.extend(root.right)

    '''
    tricky one each time 
    we will return True no matter what 
    if we do return c1 and c2 and c3 
    then it will add more than 2 values in parents 
    '''
    return condition1 and condition2 and condition3


def correctBST(root):
    # trying to store parents of wrong nodes 
    # add then swapping their values
    parents = []
    min_, max_ = 0, 100 # according to constraints
    ans = is_bst(root, parents, min_, max_)
    if len(parents) != 2:
        return root

    node1, node2 = parents
    temp = node1.data
    node1.data = node2.data
    node2.data = temp

    return root