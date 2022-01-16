'''
https://practice.geeksforgeeks.org/problems/subset-sum-problem/0
'''




'''
def is_partition(sum_, i):
    if sum_ == 0:
        return True

    if i > n-1 or sum_ < 0:
        return False

    num = nums[i]
    return is_partition(sum_-num, i+1) or is_partition(sum_, i+1)

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))

        sum_ = sum(nums)
        if sum_ % 2 == 1:
            print('NO')
        else:
            sum_ = sum_ // 2
            ans = is_partition(sum_, 0)
            if ans:
                print('YES')
            else:
                print('NO')
'''

def is_partition(sum_, i):
    # 2 lines saves the day
    if cache[sum_][i] is not None:
        return cache[sum_][i]

    if sum_ == 0:
        return True

    if i > n-1 or sum_ < 0:
        return False

    num = nums[i]
    cache[sum_][i] = is_partition(sum_-num, i+1) or is_partition(sum_, i+1)
    return cache[sum_][i]


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))

        sum_ = sum(nums)

        if sum_ % 2 == 1:
            print('NO')
        else:
            sum_ = sum_ // 2

            cache = [[None]*(n+1) for i in range(sum_+1)]
            ans = is_partition(sum_, 0)
            if ans:
                print('YES')
            else:
                print('NO')