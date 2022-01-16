'''
https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1/
'''


def removeTheLoop(head):
    if head is None or head.next is None:
        return
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # in case there was a loop
    if slow == fast:
        slow = head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None

