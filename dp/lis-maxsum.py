'''
https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0
'''

def lis_maxsum(nums, n):
    cache = [num for num in nums]

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and (cache[j] + nums[i]) > cache[i]:
                cache[i] = cache[j] + nums[i]
    print(max(cache))



if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        lis_maxsum(nums, n)
