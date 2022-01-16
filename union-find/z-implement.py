'''
https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/
'''



def root(i):
    while lis[i] != i:
        i = lis[i]
    return i


def find(a, b):
    return root(a) == root(b)


def union(a, b):
    root_a = root(a)
    root_b = root(b)

    if size[root_a] < size[root_b]:
        lis[root_a] = lis[root_b]
        size[root_b] += size[root_a]
    else:
        lis[root_b] = lis[root_a]
        size[root_a] += size[root_b]


if __name__ == '__main__':
    lis = [0, 1, 2, 3, 4, 5]
    size = [1, 1, 1, 1, 1, 1]
    # n = int(input())
    # for i in range(n):
    #     lis.append(i)
    #     size.append(1)  # it is 1 not i 
    union(0, 1)
    union(1, 2)
    union(3, 2)
#    print(find(0,1))
    print(size)
    print(lis)
