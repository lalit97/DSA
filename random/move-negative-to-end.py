'''
https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end/0/
'''



def move_negatives(lis, n):
    temp = []

    for item in lis:
        if item >=0:
            temp.append(item)
    for item in lis:
        if item < 0:
            temp.append(item)
    print(*temp)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        lis = list(map(int,input().split()))
        move_negatives(lis, n)
