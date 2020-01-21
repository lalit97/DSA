






from collections import defaultdict


def diagonalPrint(root):
    key = 0
    dict_ = defaultdict(list)
    preorder(root, key, dict_)
    ordered_keys = sorted(dict_)
    for item in ordered_keys:
        print(*dict_[item], end=' ')



def preorder(root, key, dict_):
    if root is not None:
        dict_[key].append(root.data)
        preorder(root.left, key+1, dict_)
        preorder(root.left, key, dict_)
