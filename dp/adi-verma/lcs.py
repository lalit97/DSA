
def longestCommonSubsequence(n, m):
    t = [[-1]*(m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            else:
                if str1[i-1] == str2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
    return n - t[-1][-1]


if __name__ == '__main__':
    for _ in range(int(input())):
        str1 = input()
        str2 = str1[::-1]
        n = len(str1)
        m = n
        print(longestCommonSubsequence(n, m))
