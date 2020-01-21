'''
https://practice.geeksforgeeks.org/problems/special-stack/1

using o(N) extra space
https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/

o(1) o(1)
https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
'''


# function should append an element on to the stack
def push(arr, ele):
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    if not arr:
        return
    arr.pop()

# function should return minimum element from the stack
def getMin(n, arr):
    return min(arr)
