'''
https://practice.geeksforgeeks.org/problems/wave-array/0
'''



def print_wave(lis, n):
    i = 0
    while i + 2 < n:
        lis[i], lis[i+1] = lis[i+1], lis[i]
        i += 2
    if n % 2 == 0:
        lis[-1], lis[-2] = lis[-2], lis[-1]
    print(*lis)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        lis = input().split()
        print_wave(lis, n)
        