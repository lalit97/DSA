'''
https://practice.geeksforgeeks.org/problems/non-repeating-element/0
'''


from collections import Counter

def non_reapeat(lis, n):
    d = Counter(lis)

    for item in lis:
        if d.get(item) == 1:
            return item 

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        lis = list(map(int,input().split()))
        print(non_reapeat(lis, n))
