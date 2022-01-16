
from collections import deque

def first_non_repeat(string, n):
    queue = deque()
    lookup = set()
    searched = set()

    ans = string[0]
    flag = False
    for char in string:
        if char not in lookup:
            lookup.add(char)
            queue.append(char)
            if flag:
                ans = queue[0]
                flag = False
        else:
            if char == ans:  # a b b c
                if queue:
                    queue.popleft()
                if queue:
                    ans = queue[0]
                else:
                    ans = -1
                    flag = True  # we have to check to change ans in this case
            else:
                if char not in searched:
                    searched.add(char)
                    if char in queue:
                        queue.remove(char)

        print(ans, end=' ')


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        string = input().split()
        first_non_repeat(string, n)
        print()