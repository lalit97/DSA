'''
https://practice.geeksforgeeks.org/problems/delete-keys-in-a-linked-list/1
'''



def deleteAllOccurances(head, k):
    if head is None:
        return None
    if head.next is not None and head.data == k:
        head = head.next

    current = head
    while current is not None and current.next is not None:
        if current.data == k:  # in case of 2 or more consecutive deletions
            current.data = current.next.data
            to_del = current.next
            current.next = current.next.next
            to_del.next = None
        elif current.next.data == k:
            to_del = current.next
            current.next = current.next.next
            to_del.next = None
        else:
            current = current.next
    return head
