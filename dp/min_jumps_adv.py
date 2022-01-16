'''
https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0
'''


# purely correct. 



def min_jumps(index):
    if cache[index] != -1:
        return cache[index]


    if index > n-1:
        return n + 1  # so this answer can not win in min() call

    dist = nums[index]
    nums_ahead = n - (index+1)
    if dist == 0:
        return n + 1
    if dist >= nums_ahead:
        return 1   # it can cover it in one go 


    cache[index] = min(
            [min_jumps(index+k) + 1 for k in range(1, dist+1)]
        )

    return cache[index]
    

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        
        cache = [-1 for i in range(n)]
        ans = min_jumps(0)
        if ans > n:
            print(-1)
        else:
            print(ans)



'''

def minJumps(arr, l, h): 
    if (h == l): 
        return 0
  
    if (arr[l] == 0): 
        return float('inf') 

    min = float('inf') 
    for i in range(l + 1, h + 1): 
        if (i < l + arr[l] + 1): 
            jumps = minJumps(arr, i, h) 
            if (jumps != float('inf') and 
                       jumps + 1 < min): 
                min = jumps + 1
  
    return min
  

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        ans = minJumps(nums, 0, n-1)
        if ans > n:
            print(-1)
        else:
            print(ans)
'''
