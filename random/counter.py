'''
https://practice.geeksforgeeks.org/problems/frequency-of-array-elements/0
'''


def counter(lis, n):
    d = {}
    for i in range(1, n+1):
        d[i] = 0

    for item in lis:
        d[item] += 1

    print(*d.values())


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        lis = list(map(int,input().split()))
        counter(lis, n)
