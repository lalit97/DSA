'''
https://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0

https://www.youtube.com/watch?v=VmogG01IjYc&list=PLI1t_8YX-Apv-UiRlnZwqqrRT8D1RhriX&index=11


https://leetcode.com/problems/find-median-from-data-stream/discuss/333680/Python-standard-implementation.-Commented.-Explained-%3A)
'''


from math import floor as f
import heapq


def add_number(number, lowers, highers):
    if len(lowers) == 0 or number < -lowers[0]:
        heapq.heappush(lowers, -number)
    else:
        heapq.heappush(highers, number)


def rebalance(lowers, highers):
    len_lower, len_higher = len(lowers), len(highers)
    if len_lower - len_higher == 2:
        item_to_move = -heapq.heappop(lowers)
        heapq.heappush(highers, item_to_move)
    elif len_higher - len_lower == 2:
        item_to_move = heapq.heappop(highers)
        heapq.heappush(lowers, -item_to_move)


def get_median(lowers, highers):
    len_lower, len_higher = len(lowers), len(highers)
    if len_lower == len_higher:
        left = -1 * lowers[0]
        right = highers[0]
        return f((left + right) /2)
    elif len_lower > len_higher:
        return -1 * lowers[0]
    else:
        return highers[0]



if __name__ == '__main__':
    lowers = []
    highers = []
    heapq.heapify(lowers)
    heapq.heapify(highers)

    for i in range(int(input())):
        item = int(input())
        add_number(item, lowers, highers)
        rebalance(lowers, highers)
        ans = get_median(lowers, highers)
        print(ans)