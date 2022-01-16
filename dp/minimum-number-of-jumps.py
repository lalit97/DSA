'''
https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0
'''

#v1

def min_jumps(index, nums_ahead):
    if index > n-1:
        return n + 1  # so this answer can not win in min() call

    dist = nums[index]
    if dist >= nums_ahead:
        return 1   # it can cover it in one go 

    return min([min_jumps(index+k, nums_ahead-k) + 1 for k in range(1, dist+1)])


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))

        print(min_jumps(0, n-1))


'''
v2
actually we can reduce arguments here.
'''

def min_jumps(index):
    if index > n-1:
        return n + 1  # so this answer can not win in min() call

    nums_ahead = n - (index + 1)
    dist = nums[index]
    if dist >= nums_ahead:
        return 1   # it can cover it in one go 

    return min([min_jumps(index+k) + 1 for k in range(1, dist+1)])


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))

        if 0 in nums:
            print(-1)
        else:
            print(min_jumps(0))


# v3 -> Trying to change the return call statement

def min_jumps(index):
    if index > n-1:
        return n + 1  # so this answer can not win in min() call

    nums_ahead = n - (index + 1)
    dist = nums[index]
    if dist >= nums_ahead:
        return 1   # it can cover it in one go 

    temp = []
    for k in range(1, dist+1):
        temp.append(min_jumps(index+k) + 1)
    return min(temp)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))

        if 0 in nums:
            print(-1)
        else:
            print(min_jumps(0))



# v4  Tabulation

def min_jumps(index):
    if cache[index] != -1:
        return cache[index]

    if index > n-1:
        return n + 1  # so this answer can not win in min() call

    nums_ahead = n - (index + 1)
    dist = nums[index]

    if dist == 0:
        return n + 1

    if dist >= nums_ahead:
        return 1        # it can cover it in one go 

    temp = []
    for k in range(1, dist+1):
        cache[index+k] = min_jumps(index+k) + 1
        temp.append(cache[index+k])
    return min(temp)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))

        if 0 in nums:
            print(-1)
        else:
            cache = [-1 for i in range(n)]
            print(min_jumps(0))
