'''
https://practice.geeksforgeeks.org/problems/nth-catalan-number/0
'''


def fill_cache(n):
    cache[0] = 1
    cache[1] = 1


    for i in range(2, n+1):
        cache[i] = 0
        for j in range(i):
            ans = cache[j] * cache[i-j-1]
            cache[i] = cache[i] + ans         


if __name__ == '__main__':
    n = 101
    cache = [0] * (n+1)
    fill_cache(n)

    for _ in range(int(input())):
        q = int(input())
        print(cache[q])