'''
https://practice.geeksforgeeks.org/problems/operations-on-binary-min-heap/1
'''
'''
heap = [0 for i in range(101)]  # our heap to be used
'''
from math import floor as f 


def min_heapify(index, curr_size):
    left = 2 * index + 1
    right = (2 * index) + 2

    if left <= curr_size-1 and heap[left] < heap[index]:
        smallest = left
    else:
        smallest = index

    if right <= curr_size-1 and heap[smallest] > heap[right]:
        smallest = right

    if smallest != index:
        heap[smallest], heap[index] = heap[index], heap[smallest]
        min_heapify(smallest, curr_size)


def insertKey(x):
    '''
    :param x: Insert value in heap.
    :return: None
    '''
    global curr_size
    heap[curr_size] = x

    curr = curr_size
    while (curr >= 0 and heap[f((curr-1)/2)] > heap[curr]):
        heap[f((curr-1)/2)], heap[curr] = heap[curr], heap[f((curr-1)/2)]
        curr = f((curr-1)/2)

    curr_size += 1



def deleteKey(x):
    '''
    :param x: Index of value to be removed from heap.
    :return: None
    '''
    global curr_size
    if x > curr_size -1:
        return

    heap[x], heap[curr_size-1] = heap[curr_size-1], heap[x]
    del heap[curr_size-1]

    curr_size -= 1
    min_heapify(x, curr_size)


def extractMin():
    '''
    :return: return the minimum element from heap and remove it.
    '''
    global curr_size
    if curr_size <= 0: # first is None so basically zero elements there
        return -1
    minimum = heap[0]
    deleteKey(0)
    return minimum