'''
https://www.hackerrank.com/challenges/game-of-two-stacks/problem
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

def create_stack(lis):
    MyStack = Stack()
    for item in lis[::-1]:
        MyStack.push(item)
    return MyStack


def stack_game(m,n,x):
    count, sum = -1, 0
    while sum <= x:
        if m.top is not None and n.top is not None:
            if m.top.data <= n.top.data:
                item = m.pop()
            else:
                item = n.pop()
        elif m.top is not None:
            item = m.pop()
        elif n.top is not None:
            item = n.pop()
        else:
            return count
        sum += item
        count += 1
    return count


def twoStacks(x, a, b):
    m = create_stack(a)
    n = create_stack(b)
    res = stack_game(m,n,x)
    return res

if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        print(result)