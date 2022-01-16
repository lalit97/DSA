'''
https://practice.geeksforgeeks.org/problems/find-the-closest-pair-from-two-arrays/0/
'''

def closest_pair(lis1, lis2, k, n, m):
    i, j = 0, m-1
    closest = 10000000
    ans = (None, None)
    while i < n and j < m:
        first = lis1[i]
        second = lis2[j]
        p_sum = first + second

        check = k - p_sum
        diff = abs(p_sum - k)

        if diff > closest:
            break

        if diff < closest:
            closest = diff
            ans = (first, second)

        if check < 0:
            j -= 1
        elif check > 0:
            i += 1
        else:
            break

    print(*ans)

if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        lis1 = list(map(int,input().split()))
        lis2 = list(map(int,input().split()))
        k = int(input())
        closest_pair(lis1, lis2, k, n, m)
