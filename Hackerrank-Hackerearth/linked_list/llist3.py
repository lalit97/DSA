'''
https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
'''

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)


def insertNodeAtHead(llist, data):
    head = llist
    if head is None:
        head = SinglyLinkedListNode(data)
        return head 
    else:
        current = SinglyLinkedListNode(data)
        current.next = head
        return current


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.head = insertNodeAtHead(llist.head, llist_item)
    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')
    fptr.close()
