'''
https://www.hackerrank.com/challenges/balanced-brackets/problem

https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
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
        to_del = self.top
        self.top = self.top.next
        to_del = None
        return item


def isBalanced(s):
    MyStack = Stack()
    for item in s:
        if (item == '{') or (item =='[') or (item == '('):
            MyStack.push(item)
        else:
            top = MyStack.pop()
            print(item, top)
            if top is not None:
                cond1 = item == ')' and top == '('
                cond2 = item == '}' and top == '{'
                cond3 = item == ']' and top == '['
                if not cond1 and not cond2 and not cond3:
                    return 'NO'
            else:
                return 'NO'  # handling the case '[{}]))'
    if MyStack.top is None:
        return 'YES'
    else:
        return 'NO'  # handling the case '[{}](('


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()
