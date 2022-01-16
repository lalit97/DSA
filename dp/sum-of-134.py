'''
https://practice.geeksforgeeks.org/problems/count-ways-to-express-n-as-the-sum-of-13-and-4/0
'''


def fill_cache(n):
    cache.extend([1,1,1,2])

    for i in range(4, n):

        #checking past
        ans = (cache[i-1] % mod) + (cache[i-3] % mod) + (cache[i-4] % mod)
        ans = ans % mod
        cache.append(ans)


if __name__ == '__main__':
    n = 100001
    mod = 10**9 + 7
    cache = []
    fill_cache(n)

    for _ in range(int(input())):
        q = int(input())
        print(cache[q])