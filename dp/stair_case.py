'''
https://practice.geeksforgeeks.org/problems/count-ways-to-reach-the-nth-stair/0
'''
'''
def staircase(index):
    if index > n:
        return 0
    if index == n:
        return 1

    return staircase(index+1) + staircase(index+2)
'''

'''
This is one is so easy to convert into a bottom up
def staircase(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return staircase(n-1) + staircase(n-2)
'''

'''
In Memoization cache size is decided by seeing function calls in recursive solution 
we have to store every function call that simple.

'''

'''
def staircase(index):
    if index > n:
        return 0
    if index == n:
        return 1

    if cache[index] != -1:
        return cache[index]

    cache[index] = staircase(index+1) + staircase(index+2)
    return cache[index]


if __name__ == '__main__':
    mod = 10**9 + 7
    for _ in range(int(input())):
        n = int(input())
        cache = [-1 for i in range(n)]
        print(staircase(0))

'''



def staircase(n):
    mod = 10**9 + 7

    cache[0] = 1 
    cache[1] = 1

    for i in range(2, n+1):
        ans = (cache[i-1] % mod)  + (cache[i-2] % mod)
        cache[i] = ans % mod


if __name__ == '__main__':
    n = 100000
    cache = [0 for i in range(n+1)]
    staircase(n)
    for _ in range(int(input())):
        n = int(input())
        print(cache[n])