'''
https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/b-sequence-f919fc86/
'''

n = int(input())
lis = list(map(int, input().split()))

max_item, max_index = 0, 0
for i in range(n):
    if lis[i] > max_item:
        max_item = lis[i]
        max_index = i

increasing = set(lis[:(max_index+1)])
decreasing = set(lis[(max_index+1):])

for i in range(int(input())):
    item = int(input())
    if item == max_item:
        pass
    elif item in increasing and item in decreasing:
        pass
    elif item not in increasing:
        if item > max_item:
            max_item = item 
        increasing.add(item)
        n += 1
    else:
        decreasing.add(item)
        n += 1
    print(n)

start = sorted(increasing)
end = sorted(decreasing, reverse=True)
print(*start, *end, sep=' ')
