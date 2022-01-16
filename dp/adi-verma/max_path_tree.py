"""
leetcode
"""


class Solution:
    def __init__(self):
        self.result = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        self.solve(root)
        return self.result

    def solve(self, root):
        if root is None:
            return 0
        l = self.solve(root.left)
        r = self.solve(root.right)

        temp = max(max(l, r) + root.val, root.val)
        ans = max(l + r + root.val, temp)
        self.result = max(self.result, ans)
        return temp


###################################
result = None


def solve(root):
    global result
    if root is None:
        return 0
    l = solve(root.left)
    r = solve(root.right)

    temp = max(max(l, r) + root.data, root.data)
    ans = max(l + r + root.data, temp)
    result = max(ans, result)
    return temp


def findMaxSum(root):
    global result
    result = float("-inf")
    solve(root)
    return result
