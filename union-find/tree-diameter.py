
def height(root, cache):
    if root is None:
        return 0
    cache[root] = 1 + max(height(root.left, cache), height(root.right, cache))
    return cache[root]


def dia_help(root, cache):
    if root is None:
        return 0
    direct = 1 + cache.get(root.left, 0) + cache.get(root.right, 0)
    left_dia = dia_help(root.left, cache)
    right_dia = dia_help(root.right, cache)

    return max(direct, left_dia, right_dia)


def diameter(root):
    cache = {}
    if root is None:
        return 0
    height(root, cache)
    return dia_help(root, cache)