'''
https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

done without help.

'''
class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)


def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if head is None:
        head = new_node
        return head

    current = head
    while current.next is not None:
        #at the start of list 
        if data <= current.data:
            new_node.next = current
            new_node.prev = None
            current.prev = new_node
            head = new_node  # special case we have new head now!
            return head 
        
        #somewhere in the middle
        elif data > current.data and data <= current.next.data:
            new_node.prev = current
            new_node.next = current.next 
            current.next = new_node
            new_node.next.prev = new_node
            return head
        current = current.next

    #at the end of list     
    new_node.next = None
    new_node.prev = current
    current.next = new_node
    return head




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        llist_count = int(input())
        llist = DoublyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        data = int(input())
        llist1 = sortedInsert(llist.head, data)
        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')
    fptr.close()
