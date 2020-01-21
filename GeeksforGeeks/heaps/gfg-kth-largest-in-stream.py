'''
https://medium.com/@lenchen/leetcode-703-kth-largest-element-in-a-stream-194ceb1572
https://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream/0
https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/148866/Python-simple-heapq-solution-beats-100

idea is to keep only k items in heap.
and build a min heap out of it.
'''

import heapq


def kth_largest(lis, n, k):
    heap = []
    '''
    from start to k-1 items keep pushing 
    into heap and keep priniting -1
    because not sufficient elements to find kth_largest
    '''
    for i in range(k-1):  # till when there are not k elements
        print(-1, end=' ')
        heapq.heappush(heap, lis[i])

    '''
    now there are k-1 elements, push the kth element
    now you can print heap[0] this will be kth minimum
    '''
    heapq.heappush(heap, lis[k-1])
    print(heap[0], end=' ')

    '''
    for further elements 2 cases possible if the next elements
    is less then the heap[0] then it won't contribute in calculation
    of kth_largest element
    
    otherwise if it is greater than it will contribute
    so now there will be new answer, remove top and add the item in heap
    now print heap[0]
    '''
    for i in range(k, n):
        item = lis[i]
        if item > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, item)
        print(heap[0], end=' ')


if __name__ == '__main__':
    for _ in range(int(input())):
        k, n = map(int, input().split())
        lis = list(map(int, input().split()))
        kth_largest(lis, n, k)
        print()