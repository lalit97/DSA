'''
https://practice.geeksforgeeks.org/problems/rearrange-characters/0

https://leetcode.com/problems/reorganize-string/discuss/384051/easy-peasy-python-heap-priority-queue-(100)

https://leetcode.com/problems/reorganize-string/discuss/456020/Python-Heap-Easy-to-understand-self-explanatory-code'''

import heapq
from collections import Counter


def rearrange_chars(string):
    d = Counter(string)
    heap = []
    for key, value in d.items():
        heap.append((-value,key))
    heapq.heapify(heap)


    result = ''
    prev = heapq.heappop(heap)
    result += prev[1]
    while heap: 
        curr = heapq.heappop(heap)
        result += curr[1]

        if prev[0] + 1 < 0:
            heapq.heappush(heap,(prev[0]+1, prev[1]))
        prev = curr


    if len(result) != len(string):
        return 0
    else:
        return 1


if __name__ == '__main__':
    for _ in range(int(input())):
        print(rearrange_chars(input()))
