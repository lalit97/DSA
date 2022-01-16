'''
https://practice.geeksforgeeks.org/problems/nth-fibonacci-number/0
'''


def fill_cache(n):
    cache.extend([None,1,1])

    for i in range(3, n):

        #checking past
        ans = (cache[i-1] % mod) + (cache[i-2] % mod)         
        ans = ans % mod
        cache.append(ans)


if __name__ == '__main__':
    n = 1001
    mod = 10**9 + 7
    cache = []
    fill_cache(n)

    for _ in range(int(input())):
        q = int(input())
        print(cache[q])