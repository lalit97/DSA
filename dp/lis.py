'''
https://leetcode.com/problems/longest-increasing-subsequence/discuss/300914/Python-DP-Easy

https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
'''


def longest_increasing(nums, n):
    cache = [1] * n
    for i in range(1, n):
        for j in range(i):  # checking past
            if nums[i] > nums[j] and cache[j] + 1 > cache[i]:
                cache[i] = cache[j] + 1
    print(max(cache))
    #print(cache)

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        longest_increasing(nums, n)