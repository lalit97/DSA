'''
https://www.hackerrank.com/challenges/maximum-element/problem

https://www.geeksforgeeks.org/tracking-current-maximum-element-in-a-stack/
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
        to_del = self.top
        if self.top is None:
            return False
        item = self.top.data
        self.top = self.top.next
        to_del = None
        return item


if __name__ == '__main__':
    MyStack = Stack()
    MaxStack = Stack()
    for i in range(int(input())):
        s = input().split()
        if i == 0:
            item = int(s[1])
            MyStack.push(item)
            MaxStack.push(item)
        else:
            if s[0] == '2':
                MyStack.pop()
                MaxStack.pop()
            elif s[0] == '3':
                print(MaxStack.top.data)
            else:
                a,b = map(int, s)
                MyStack.push(b)
                if MaxStack.top is None:
                    MaxStack.push(b)
                elif b > MaxStack.top.data:
                    MaxStack.push(b)
                else:
                    item = MaxStack.top.data
                    MaxStack.push(item)
