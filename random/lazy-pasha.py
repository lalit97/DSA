'''
https://practice.geeksforgeeks.org/problems/lazy-pasha/0/

https://www.geeksforgeeks.org/left-rotation-right-rotation-string-2/
https://stackoverflow.com/questions/4457277/algorithm-to-rotate-an-array-in-linear-time
'''

def reverse(string, start, end):
    while  end > start:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1


def left_rotate(string, d, length):
    reverse(string, 0, d-1)
    reverse(string, d, length-1)
    reverse(string, 0, length-1)


def rotate_string(string, length, dist):
    left_rotate(string, length-dist, length)


def print_char(string, length, dist):
    return string[dist]
    

if __name__ == '__main__':
    for _ in range(int(input())):
        length, query = map(int, input().split())
        string = list(input())
        for i in range(query):
            val, dist = map(int, input().split())
            if val == 1:
                rotate_string(string, length, dist)
            else:
                print(print_char(string, length, dist))