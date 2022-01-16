



def fill_cache(n):
    cache[0] = 1
    i2, i3, i5 = 0, 0, 0
    next_2 = cache[i2] * 2
    next_3 = cache[i3] * 3
    next_5 = cache[i5] * 5

    for index in range(1, n):
        next_ugly = min(next_2, next_3, next_5)
        cache[index] = next_ugly

        if next_ugly == next_2:
            i2 += 1
            next_2 = cache[i2] * 2 
        
        if next_ugly == next_3:
            i3 += 1
            next_3 = cache[i3] * 3
        
        if next_ugly == next_5:
            i5 += 1
            next_5 = cache[i5] * 5


if __name__ == '__main__':
    n = 10000
    cache = {}  # fast lookup :)
    fill_cache(n)

    for _ in range(int(input())):
        n = int(input())
        print(cache[n-1])
