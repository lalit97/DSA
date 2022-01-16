

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None


    def append(self, data):
        new_node = Node(data)
        if self.last is not None:
            self.last.next = new_node
        self.last = new_node
        if self.first is None:
            self.first = self.last


    def appendleft(self, data):  #O(1)
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
        new_node.next = self.first
        self.first = new_node


    def popleft(self):
        if self.first is None:
            return None

        item = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None
        return item


    def pop(self):  # O(n)
        if self.last is None:
            return None
        if self.first is None:
            return None
        
        current = self.first
        while current.next != self.last:
            current = current.next

        item = current.next.data
        self.last = current
        self.last.next = None

        return item


    def peek(self):
        if self.first is None:
            return None
        return self.first.data


    def is_empty(self):
        return self.first == None


    def traverse(self):
        if self.first is None:
            return None
        current = self.first
        while current is not None:
            print(current.data, end=' ')
            current = current.next


if __name__ == '__main__':
    q = Queue()
    q.append(5)
    q.append(10)
    q.append(15)
    q.append(20)
    q.popleft()
    q.popleft()
    q.appendleft(12)
    q.appendleft(14)
    q.pop()
    q.traverse()
