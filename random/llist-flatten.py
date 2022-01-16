'''
https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1
'''



'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    nums = []
    while root is not None:
        curr = root
        while curr is not None:
            nums.append(curr.data)
            curr = curr.bottom
        root = root.next

    sorted_nums = sorted(nums)
    new_head = Node(sorted_nums[0])
    curr = new_head
    for item in sorted_nums[1:]:
        curr.bottom = Node(item)
        curr = curr.bottom
    return new_head