'''
https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/little-monk-and-swaps/

https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/

https://www.geeksforgeeks.org/minimum-swap-required-convert-binary-tree-binary-search-tree/

https://stackoverflow.com/questions/41622174/inorder-binary-tree-traversal-using-python

https://www.geeksforgeeks.org/minimum-number-of-swaps-required-to-sort-an-array-set-2/

'''
from collections import deque


class Node:
    def __init__(self, val):
        self.info = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.info)


class BinaryTree:
    def __init__(self):
        self.queue = deque()
        self.root = None

    def create(self, lis, n):
        queue = self.queue
        current = self.root
        queue.append(current)
        for i in range(n):
            if (2*i+1) < n:
                current = queue.popleft()
                current.left = Node(lis[2*i+1])
                current.right = Node(lis[2*i+2])
                queue.append(current.left)
                queue.append(current.right)
            else:
                break


def in_order(root):
    res = []
    if root:
        res = in_order(root.left)
        res.append(root.info)
        res = res + in_order(root.right)
    return res


def swap_count(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps


if __name__ == '__main__':
    # n = int(input())
    # lis = list(map(int, input().split()))
    # tree = BinaryTree()
    # tree.root = Node(lis[0])
    # tree.create(lis, n)
    # res = in_order(tree.root)
    # print(res)
    lis = [1,3,5,2,4,6,8]
    print(swap_count(lis))