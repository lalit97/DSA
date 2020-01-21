'''
Resource --> CTCI
and learning from hackerrank linked lists

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node


    def pop(self):
        if self.top is None:
            return None
        item = self.top.data
        self.top = self.top.next
        return to_del.data


    def peek(self):
        if self.top is None:
            return None
        return self.top.data


    def traverse(self):
        if self.top is None:
            return None
        current = self.top
        while current is not None:
            print(current.data, end=' ')
            current = current.next

    def is_empty(self):
        return self.top == None


if __name__ == '__main__':
    MyStack = Stack()
    MyStack.push(5)
    MyStack.push(10)
    MyStack.push(15)
    MyStack.push(25)
    MyStack.push(35)
    MyStack.pop()
    MyStack.pop()
    MyStack.pop()
    MyStack.traverse()