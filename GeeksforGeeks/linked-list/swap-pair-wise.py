'''
https://practice.geeksforgeeks.org/problems/pairwise-swap-elements-of-a-linked-list-by-swapping-data/1/
'''


def pairWiseSwap(head):
    if head is None or head.next is None:
        return head
    current = head
    while current is not None and current.next is not None:
        temp = current.next.data
        current.next.data = current.data
        current.data = temp

        current = current.next.next
    return head