


def solve(e, f):
    if f == 1 or f == 0:
        return f
    if e == 1:
        return f

    if t[e][f] != -1:
        return t[e][f]

    ans = float('inf')
    for k in range(1, f):
        temp = 1 + max(solve(e-1, k-1), solve(e, f-k))
        ans = min(temp, ans)

    t[e][f] = ans
    return t[e][f]


if __name__ == '__main__':
    for _ in range(int(input())):
        e,f = map(int, input().split())
        ans = float('inf')
        t = [[-1]*(f+1) for i in range(e+1)]
        print(solve(e, f))