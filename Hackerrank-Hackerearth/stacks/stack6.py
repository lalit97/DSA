'''
https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/a-game-of-numbers-1-5d3a8cb3/

https://www.ideserve.co.in/learn/next-great-element-in-an-array (good one)

https://www.geeksforgeeks.org/next-greater-element/

https://www.geeksforgeeks.org/find-next-smaller-next-greater-array/
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        to_del = self.top
        item = to_del.data
        to_del = None 
        self.top = self.top.next
        return item

if __name__ == '__main__':
