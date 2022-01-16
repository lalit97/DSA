


def solve(i, j, is_true): 
    if i > j:
        return False
    if i == j:
        if is_true:
            return exp[i] == 'T'
        return exp[i] == 'F'

    if t[i][j][is_true] != -1:
        return t[i][j][is_true]

    ans = 0
    for k in range(i+1, j, 2):
        if t[i][k-1][True] == -1:
            lt = solve(i, k-1, True)
        else:
            lt = t[i][k-1][True]
        if t[i][k-1][False] == -1:
            lf = solve(i, k-1, False)
        else:
            lf = t[i][k-1][False]
        if t[k+1][j][True] == -1:
            rt = solve(k+1, j, True)
        else:
            rt = t[k+1][j][True]
        if t[k+1][j][False] == -1:
            rf = solve(k+1, j, False)
        else:
            rf = t[k+1][j][False]


        if exp[k] == '|':
            if is_true:
                ans += (lt * rt)% 1003 + (lt * rf)% 1003 + (lf * rt)% 1003
            else:
                ans += (lf * rf)% 1003
        elif exp[k] == '&':
            if is_true:
                ans += (lt * rt)% 1003
            else:
                ans += (lf * rf)% 1003 + (lt * rf)% 1003 + (lf * rt)% 1003
        else:
            if is_true:
                ans += (lt * rf)% 1003 + (lf * rt)% 1003
            else:
                ans += (lf * rf)% 1003 + (lt * rt)% 1003
    t[i][j][is_true] = ans % 1003
    return t[i][j][is_true] % 1003


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        exp = input()
        ans = 0
        i, j = 0, n-1
        t = [[[-1]*2 for i in range(n+1)]for i in range(n+1)]
        print(solve(i, j, True))