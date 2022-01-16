def count_subset_sum(n, s):
    t = [[-1]*(s+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if j == 0:
                t[i][j] = 1
            elif i == 0:
                t[i][j] = 0
            else:
                if j >= nums[i-1]:
                    t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
    return t

if __name__ == '__main__':
    nums = [9,7,0,3,9,8,6,5,7,6]
    n = 10
    s = 31
    mt = count_subset_sum(n, s)
    for lis in mt:
        print(lis)