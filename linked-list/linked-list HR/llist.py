class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        

def printLinkedList(head):
    if head is not None:
        print(head.data)
        printLinkedList(head.next)


if __name__ == '__main__':
    n = int(input())
    llist = SinglyLinkedList()
    for _ in range(n):
        llist_item = int(input())
        llist.insert_node(llist_item)
    printLinkedList(llist.head)
