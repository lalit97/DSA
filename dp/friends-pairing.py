'''
https://practice.geeksforgeeks.org/problems/friends-pairing-problem/0
'''


def fill_cache(n):
    cache.extend([0,1,2])

    for i in range(3, n):

        #checking past
        first = cache[i-1] % mod  
        second = (((i-1) % mod) * (cache[i-2] % mod)) % mod         
        ans = (first + second) % mod
        cache.append(ans)


if __name__ == '__main__':
    n = 101
    mod = 10**9 + 7
    cache = []
    fill_cache(n)

    for _ in range(int(input())):
        q = int(input())
        print(cache[q])