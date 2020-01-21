'''
made with help of 
https://www.hackerearth.com/practice/notes/heaps-and-priority-queues/

and 
Siddhesh Suthar
'''
from math import floor as f


def max_heapify(lis, index, n):
    left = 2 * index
    right = 2 * index + 1

    if left <= n and lis[left] > lis[index]:
        largest = left
    else:
        largest = index
    if right <= n and lis[right] > lis[largest]:
        largest = right

    if largest != index:
        lis[index], lis[largest] = lis[largest], lis[index]
        max_heapify(lis, largest, n)


def min_heapify(lis, index, n):
    left = 2 * index
    right = 2 * index + 1

    if left <= n and lis[left] < lis[index]:
        smallest = left
    else:
        smallest = index
    if right <= n and lis[right] < lis[smallest]:
        smallest = right

    if smallest != index:
        lis[index], lis[smallest] = lis[smallest], lis[index]
        min_heapify(lis, smallest, n)



if __name__ == '__main__':
    n = int(input())
    items = map(int, input().split())   # do not take a list here
    lis = []
    lis.append(None)  # make one based indexing
    for item in items:
        lis.append(item)

    start, stop, step = f(n/2), 0, -1
    for i in range(start, stop, step):
        min_heapify(lis, i, n) 
    print(*lis)
'''
bottom up approach is followed, as this is how it is.
'''
