'''
https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1/
'''




'''
    Your task is to remove duplicates from given 
    unsorted linked list.
    
    Function Arguments: head (head of the given linked list) 
    Return Type: head of the list after removing the duplicates from the list.
    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
from collections import OrderedDict

def removeDuplicates(head):
    current = head
    if current is None or current.next is None:
        return head
    dict_ = OrderedDict()
    while current is not None:
        item = current.data
        if item not in dict_:
            dict_[item] = None
        current = current.next


    for item in dict_:
        new_head = Node(item)
        break
    curr = new_head
    trick = False  # do not run the loop first time.
    for item in dict_:
        if trick:
            curr.next = Node(item)
            curr = curr.next
        trick = True
    return new_head
