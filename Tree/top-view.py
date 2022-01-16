'''
https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1


https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/
method number 2
'''


from collections import defaultdict
from operator import itemgetter

def topView(root):
    key = 0
    depth = 0
    dict_ = defaultdict(list)
    preorder(root, key, depth, dict_)
    orderd_keys = sorted(dict_)  # because we need to start from left most horizontal distance
    for item in orderd_keys:
        depth_sorted_tuple = sorted(dict_[item], key=itemgetter(0))  # if more than one print top most
        for depth_, data_ in depth_sorted_tuple:
            print(data_, end=' ')
            break


def preorder(root, key, depth, dict_):
    if root is not None:
        dict_[key].append((depth, root.data))
        preorder(root.left, key-1, depth+1, dict_)
        preorder(root.right, key+1, depth+1, dict_)
