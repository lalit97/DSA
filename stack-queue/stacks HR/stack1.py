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
        to_del = self.top
        if self.top is None:
            return False
        item = self.top.data
        self.top = self.top.next
        to_del = None
        return item

    def peek(self):
        top = self.top
        if top is None:
            return False
        return top.data

    def traverse(self):
        top = self.top 
        while top.next is not None:
            print(top.data)
            top = top.next
        print(top.data)


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