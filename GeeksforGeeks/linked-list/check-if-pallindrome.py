'''
https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1/
'''

def isPalindrome(head):
    if head is None or head.next is None:
        return True
    stack = []
    current = head
    while current is not None:
        stack.append(current.data)
        current = current.next

    while stack:
        if head.data != stack.pop():
            return False
        head = head.next
    return True