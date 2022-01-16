
# iterative + tabulation  (Bottom up)
def knapsack_bottom_up(capacity, n, weights, values):
    cache = [[0]*(n+1) for i in range(capacity+1)]

    for i in range(1, capacity+1):
        for j in range(1, n+1):
            if weights[j] > i:
                cache[i][j] = cache[i-1][j]
            else:
            cache[i][j] = max(
                    cache[j-i][j] + values[j],
                    cache[i-1][j]
                )
    return cache[capacity][n]



if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        capacity = int(input())
        weights = list(map(int, input().split()))
        values = list(map(int, input().split()))
        knapsack(capacity, n, weights, values)
