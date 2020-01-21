
'''
https://practice.geeksforgeeks.org/problems/heap-sort/1
'''


from math import floor as f
def heapify(arr, n, i):
    '''
    :param arr: original array
    :param n: size of original array
    :param i: subtree rooted at ith index
    :return: 
    '''
    left = 2 * i
    right = (2*i) + 1

    if left <= n and arr[left] > arr[i]:
        largest = left
    else:
        largest = i

    if right <= n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def buildHeap(arr,n):
    '''
    :param arr: given array
    :param n: size of array
    :return: None
    '''
    arr.insert(0, None)  # adding None
    start, stop, step = f(n/2), 0, -1
    for i in range(start, stop, step):
        heapify(arr, n, i)
    heap_sort(arr, n)
    del arr[0]  # removing None

def heap_sort(lis, n):
    start, stop, step = n, 1, -1
    heap_size = n

    for i in range(start, stop, step):
        lis[i], lis[1] = lis[1], lis[i]
        heap_size -= 1
        heapify(arr, heap_size, 1)