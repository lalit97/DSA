'''
https://practice.geeksforgeeks.org/problems/sort-by-absolute-difference/0/
'''

from operator import itemgetter

def sort_abs(lis, n, k):
    for i in range(n):
        item = lis[i]
        diff = abs(k - item)
        lis[i] = (diff, item)

    sort_according_to_diff = sorted(lis, key=itemgetter(0))
    for diff, item in sort_according_to_diff:
        print(item, end=' ')
    print()


if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        lis = [int(i) for i in input().split()]
        sort_abs(lis, n, k)
