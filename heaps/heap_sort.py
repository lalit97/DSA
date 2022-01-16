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

    if right <= n and lis[right] > lis[largest]:
        largest = right

    if largest != index:
        lis[index], lis[largest] = lis[largest], lis[index]
        max_heapify(lis, largest, n)



def build_maxheap(lis, n):
    start, stop, step = f(n/2), 0, -1
    for i in range(start, stop, step):
        max_heapify(lis, i, n)



def heap_sort(lis, n):
    '''
    stopping at 1 because we can leave 2 indeces i.e. 1 and 0 
    at 0th index there is None
    at 1st index whatever the item is it will be already at its position
    '''
    start, stop, step = n, 1, -1
    heap_size = n  
    for i in range(start, stop, step):
        lis[i], lis[1] = lis[1], lis[i]
        heap_size -= 1
        max_heapify(lis, 1, heap_size)  # to maintain max_heap



if __name__ == '__main__':
    n = int(input())
    items = map(int,input().split())
    lis = []
    lis.append(None)
    for item in items:
        lis.append(item)
    build_maxheap(lis, n)
    heap_sort(lis, n)
    print(lis)