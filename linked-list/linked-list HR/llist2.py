'''
https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
'''

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)


def insertNodeAtTail(head, data):
    if head is None:
        head = SinglyLinkedListNode(data)
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = SinglyLinkedListNode(data)
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    llist_count = int(input())
    llist = SinglyLinkedList()
    for i in range(llist_count):
        llist_item = int(input())
        llist.head = insertNodeAtTail(llist.head, llist_item)
    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')
    fptr.close()
