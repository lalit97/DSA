'''
TAG --> Dictionary

https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-his-friends/
'''

for _ in range(int(input())):
    n, x = map(int, input().split())
    l  = len(set(input().split()))
    if l == x:
        print('Good')
    elif l > x:
        print('Average')
    else:
        print('Bad')


