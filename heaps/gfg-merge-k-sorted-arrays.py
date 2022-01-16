'''
https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1
https://medium.com/@amitrajitbose/merge-k-sorted-arrays-da5a3526c8ed
'''
'''
:param a: given array
:param n: size of row and column
:return: merged sorted list
'''

import heapq


def mergeKArrays(lists,n):
    answer = []
    heap = []
    for index, lis in enumerate(lists):
        t = lis[0], index, 0
        heap.append(t)

    heapq.heapify(heap)

    while heap:
        value, list_ind, element_ind = heapq.heappop(heap)
        answer.append(value)

        try:
            lis = lists[list_ind]
            lis[element_ind + 1]

            next_tuple = (lis[element_ind + 1], list_ind, element_ind+1)
            heapq.heappush(heap, next_tuple)
        except IndexError as e:
            pass
    return answer
