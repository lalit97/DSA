'''
https://practice.geeksforgeeks.org/problems/maximum-path-sum/1

https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/
'''



result = 0
def maxPathSum(root):
    global result
    result = -10000000
    maxPathSum_helper(root)
    return result


def maxPathSum_helper(root):
    global result
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data

    left_sum = maxPathSum_helper(root.left)
    right_sum = maxPathSum_helper(root.right)

    result = max(result, left_sum + right_sum + root.data)  # update result

    return max(left_sum, right_sum) + root.data  # we can carry forward only one