'''
https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/
'''

'''
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem/0
'''

'''
Pure Recursive
def knapsack(capacity, i):
    if i > n - 1:
        return 0

    weight = weights[i]
    value = values[i]

    if weight > capacity:
        return knapsack(capacity, i+1)

    return max(
            knapsack(capacity-weight, i+1) + value,
            knapsack(capacity, i+1)
        )


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        capacity = int(input())
        weights = list(map(int, input().split()))
        values = list(map(int, input().split()))
        print(knapsack(capacity, 0))



'''

# Recursion + Memoization  (Top Down)


def knapsack(capacity, i):
    if i > n - 1 or capacity == 0:
        return 0

    weight = weights[i]
    value = values[i]

    # 2 lines saves the day
    if cache[capacity][i] != -1:
        return cache[capacity, i]

    # store and return
    if weight > capacity:
        cache[capacity][i] = knapsack(capacity, i+1)
        return cache[capacity][i]
    
    # store and return
    cache[capacity][i] = max(
            knapsack(capacity-weight, i+1) + value,
            knapsack(capacity, i+1)
        )
    return cache[capacity][i]




if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        capacity = int(input())
        weights = list(map(int, input().split()))
        values = list(map(int, input().split()))


        cache = [[-1]*(n+1) for i in range(capacity+1)]
        print(knapsack(capacity, 0))

        for arr in cache:
            print(arr)


