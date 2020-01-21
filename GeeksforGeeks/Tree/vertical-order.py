
from collections import defaultdict

def verticalOrder(root): 
    d = defaultdict(list)
    key = 0
    preorder(root, key, d)

    orderd_keys = sorted(d)
    for item in orderd_keys:
        print(*d[item], end=' ')



def preorder(root, key, d):
    if root is not None:
        d[key].append(root.data)
        preorder(root.left, key-1, d)
        preorder(root.right, key+1, d)

#########################################

'''
above does not works because of slight problem 
new solution keeping track of depth
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/430639/simple-python-solution-99.55-100
'''
from collections import defaultdict
from operator import itemgetter

def verticalOrder(root):
    dict_ = defaultdict(list)
    key = 0
    depth = 0
    preorder(root, key, depth, dict_)

    orderd_keys = sorted(dict_)
    for item in orderd_keys:
        for depth_, data_ in sorted(dict_[item], key=itemgetter(0)):  # by default sorts on basis of first column
            print(data_, end=' ')



def preorder(root, key, depth, dict_):
    if root is not None:
        dict_[key].append((depth, root.data))
        preorder(root.left, key-1, depth+1, dict_)
        preorder(root.right, key+1, depth+1, dict_)




######################################