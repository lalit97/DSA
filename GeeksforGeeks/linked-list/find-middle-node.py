'''
https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1/
'''

def findMid(head):
    length = get_length(head)
    middle = length // 2
    for i in range(middle):
        head = head.next
    return head


def get_length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count



'''
Much more better solution number 2nd
https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
using runner technique.
'''