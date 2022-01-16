'''
https://practice.geeksforgeeks.org/problems/array-subset-of-another-array/0
'''


def is_subset(lis1, lis2):
    for item in lis2:
        if item not in lis1:
            return False
    return True
    

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        lis1 = set(map(int,input().split()))
        lis2 = map(int,input().split())
        ans = is_subset(lis1, lis2)
        if ans:
            print('Yes')
        else:
            print('No')


