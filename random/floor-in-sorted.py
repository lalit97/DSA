'''
https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array/0
'''


def floor_sorted(lis, n, k):
    diff = 10**9
    flag = False
    for i in range(n):
        item = lis[i]
        curr = k - item

        if curr < 0:
            break  # array is sorted

        if curr >= 0 and curr < diff:
            diff = curr
            flag = True
            index = i

    if flag:
        print(index)
    else:
        print(-1)



if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        lis = list(map(int,input().split()))
        floor_sorted(lis, n, k)
