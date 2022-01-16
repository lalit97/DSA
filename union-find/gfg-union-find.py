'''
https://practice.geeksforgeeks.org/problems/disjoint-set-union-find/1
'''

'''
supports 1 based indexing
their find means finding root 
'''

# function should return parent of x
def find(arr, x):
    while arr[x-1] != x:
        x = arr[x-1]
    return x



# function should not return anything
def union(arr, x, z):
    root_x = find(arr, x)
    root_z = find(arr, z)

    arr[root_x-1] = arr[root_z-1]
