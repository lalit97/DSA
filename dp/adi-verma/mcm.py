


def solve(i, j):
    if i >= j:
        return 0
    if t[i][j] == -1:
        for k in range(i, j):
            temp = solve(i, k) + solve(k+1, j) + (arr[i-1] * arr[k] * arr[j])
            t[i][j] = min(temp, ans)
    return t[i][j]


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        t = [[-1]*(n+1) for i in range(n+1)]
        ans = float('inf')
        i, j = 1, n-1
        print(solve(i, j))