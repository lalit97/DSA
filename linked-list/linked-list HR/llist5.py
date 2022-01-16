'''
https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
'''
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)


def deleteNode(head, position):
    current = head
    if position == 0:
        return head.next
    else:
        for _ in range(position-1):
            current = current.next
        to_delete = current.next
        current.next = to_delete.next
        to_delete.next = None
        return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)
    position = int(input())
    llist1 = deleteNode(llist.head, position)
    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')
    fptr.close()
