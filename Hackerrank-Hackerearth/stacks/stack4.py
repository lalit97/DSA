'''
https://www.hackerrank.com/challenges/equal-stacks/problem
'''
import os


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.sum = 0

    def push(self, data):
        self.sum += data
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            return False
        item = self.top.data
        to_del = self.top
        self.top = self.top.next
        to_del = None
        return item


def create_stack(lis):
    MyStack = Stack()
    for item in lis[::-1]:
        MyStack.push(item)
    return MyStack


def equal_three(x, y, z):
    a, b, c = x.sum, y.sum, z.sum    
    while a != b or a != c:
        if a > b or a > c:
            item = x.pop()
            a -= item
        if b > c or b > a:
            item = y.pop()
            b -= item
        if c > a or c > b:
            item = z.pop()
            c -= item
    return a


def equalStacks(h1, h2, h3):
    x = create_stack(h1)
    y = create_stack(h2)
    z = create_stack(h3)
    res = equal_three(x,y,z)
    return res


if __name__ == '__main__':
    n1N2N3 = input().split()
    n1 = int(n1N2N3[0])
    n2 = int(n1N2N3[1])
    n3 = int(n1N2N3[2])
    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))
    result = equalStacks(h1, h2, h3)
    print(result)
