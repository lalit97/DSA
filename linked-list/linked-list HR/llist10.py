'''
https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-
position-from-the-tail/problem


Recursive --> 
https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/forum/comments/162710

Itrative -->
https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/forum/comments/217995

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


def getNode(head, positionFromTail):
    tortoise = head 
    pos = 0 
    while head is not None:
        if pos > positionFromTail:
            tortoise = tortoise.next
        pos += 1
        head = head.next
    return tortoise.data


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    tests = int(input())
    for tests_itr in range(tests):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        position = int(input())
        result = getNode(llist.head, position)
        fptr.write(str(result) + '\n')
    fptr.close()
