'''
https://practice.geeksforgeeks.org/problems/longest-common-substring/0
'''



def lcs(s1, s2, n, m):
    #fill zeros
    cache = [[0]*(m+1) for i in range(n+1)]

    result = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                cache[i][j] = 1 + cache[i-1][j-1]
                result = max(result, cache[i][j])

    # for array in cache:
    #     print(array)
    print(result)


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        s1 = input()
        s2 = input()
        lcs(s1, s2, n, m)