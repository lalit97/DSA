


########################################
#leetcode
########################################

def __init__(self):
    self.res = 0

def diameterOfBinaryTree(self, root: TreeNode) -> int:
    self.solve(root)
    return self.res - 1 # because they are asking number of edges

def solve(self, root):
    if root is None:
        return 0
    l = self.solve(root.left)
    r = self.solve(root.right)

    temp = 1 + max(l, r)
    ans = 1 + l + r
    self.res = max(ans, self.res)
    return temp


##########################################
#gfg
##########################################
result = 0


def solve(root):
    global result
    if root is None:
        return 0 
    l = solve(root.left)
    r = solve(root.right)

    temp = 1 + max(l, r)
    ans = 1 + l + r
    result = max(ans, result)
    return temp


def diameter(root):
    solve(root)
    return result
