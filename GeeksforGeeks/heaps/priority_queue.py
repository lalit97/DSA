'''
https://www.hackerearth.com/practice/notes/heaps-and-priority-queues/
'''
from math import floor as f

def max_heapify(lis, index, n):
    left = 2 * index
    right = (2 * index) + 1

    if left <= n and lis[left] > lis[index]:
        largest = left
    else:
        largest = index

    if right <=n and lis[right] > lis[largest]:
        largest = right

    if largest != index:
        lis[index], lis[largest] = lis[largest], lis[index]
        max_heapify(lis, largest, n)


def read_maximum(lis):
    return lis[1]


def extract_maximum(lis):
    global n 
    if n == 0:
        return None  # queue empty

    '''
    as CTCI says take top to bottom, left to right first item 
    and make it as the root.
    that item will be always present at lis[n]
    '''
    lis[1], lis[n] = lis[n], lis[1]
    n -= 1
    max_heapify(lis, 1, n)
    return lis.pop()


def insert_value(lis, value):
    '''
    we insert at the end of tree (going top to bottom, left to right)
    or we can insert it at the end of array, (same place it will be)
    now keep compairing it with the parent, if less, swap
    '''
    global n
    n += 1
    lis.append(value)
    curr_i = n
    while (curr_i > 1 and lis[f(curr_i/2)] < lis[curr_i]):
        lis[f(curr_i/2)], lis[curr_i] = lis[curr_i], lis[f(curr_i/2)]
        curr_i = f(curr_i/2)


def build_maxheap(lis, n):
    start, stop, step = f(n/2), 0, -1
    for i in range(start, stop, step):
        max_heapify(lis, i, n)


if __name__ == '__main__':
    n = int(input())
    items = map(int,input().split())
    lis = []
    lis.append(None)
    for item in items:
        lis.append(item)

    build_maxheap(lis, n)
    print(lis)
    insert_value(lis, 6)
    print(lis)
    print(extract_maximum(lis))
    print(lis)