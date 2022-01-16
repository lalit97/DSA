'''
https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1/
'''



def segregate(head):
    if head is None or head.next is None:
        return head
    counter = {
        0: 0,
        1: 0,
        2: 0
    }
    current = head
    while current is not None:
        counter[current.data] += 1
        current = current.next



    current = head
    t = 0
    while current is not None:
        if counter[t] == 0:
            t += 1
        else:
            current.data = t
            counter[t] -= 1
            current = current.next
    return head