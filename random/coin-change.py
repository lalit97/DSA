'''
https://www.geeksforgeeks.org/coin-change-dp-7/
'''



def count(n, k):
    if k == 0:
        return 1 
    if k < 0 or n == 0:
        return 0
    return count(n-1, k) + count(n, k-lis[n-1])




if __name__ == '__main__':
    lis = [1,2,3]
    n = 3
    k = 4

    print(count(n, k))