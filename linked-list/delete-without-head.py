'''
https://www.geeksforgeeks.org/delete-a-node-from-linked-list-without-head-pointer/
'''
'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

def deleteNode(curr_node):
    if curr_node is None:
        return
    next_node = curr_node.next
    curr_node.data = next_node.data
    to_delete = next_node
    curr_node.next = next_node.next
    to_delete.next = None