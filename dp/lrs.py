"""
https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence/0

https://www.geeksforgeeks.org/longest-repeated-subsequence/
"""

"""
idea -> 

just compare the string with the same string and find lcs, such that indices does not match

"""


def lrs(s, n):
    cache = [[0] * (n + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1] and i != j:
                cache[i][j] = 1 + cache[i - 1][j - 1]
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    print(cache[n][m])


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        s = input()
        lrs(s, n)
