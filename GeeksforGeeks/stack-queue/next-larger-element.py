'''
https://practice.geeksforgeeks.org/problems/next-larger-element/0

python for-else
https://www.geeksforgeeks.org/using-else-conditional-statement-with-for-loop-in-python/
'''
from collections import deque


def next_larger(lis, n):
    queue = deque()
    prev = lis[0]
    for i in range(1, n):
        item = lis[i]
        if item > prev:
            queue.append(item)
        prev = item



    for item in lis:
        if queue:
            front = queue[0]
            if item < front:
                print(front, end=' ')

            elif item == front:   # 7 8 1 4
                current = queue.popleft()
                for q_item in queue:
                    if q_item > current:
                        print(q_item, end=' ')
                        break
                else:
                    print(-1, end=' ')

            elif item > front:
                for q_item in queue:
                    if q_item > item:
                        print(q_item, end=' ')
                        break
                else:
                    print(-1, end=' ')

        else:
            print(-1, end=' ')


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        lis = list(map(int, input().split()))
        next_larger(lis, n)
        print()