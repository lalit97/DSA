'''
https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/editorial

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


def removeDuplicates(head):
    if (head is None) or (head.next is None):
        return head
    prev = head 
    current = head.next 
    while current is not None:
        if current.data == prev.data:
            temp = current.next
            prev.next = temp
            current = temp
            temp = None
        else:
            current = current.next
            prev = prev.next
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        llist_count = int(input())
        llist = SinglyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        llist1 = removeDuplicates(llist.head)
        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')
    fptr.close()
