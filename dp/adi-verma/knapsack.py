
def knapsack(n, w):
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                if i == 0:
                    t[i][j] = float('inf')
                else:
                    t[i][j] = 0
            elif j >= weights[i-1]:
                t[i][j] = min(1 + t[i][j-weights[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    if t[-1][-1] == float('inf'):
        return -1
    return t[-1][-1]


if __name__ == '__main__':
    for _ in range(int(input())):
        w, n = map(int, input().split())
        weights = list(map(int, input().split()))
        t = [[-1]*(w+1) for i in range(n+1)]
        print(knapsack(n, w))