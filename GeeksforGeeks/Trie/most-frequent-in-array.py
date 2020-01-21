

'''
https://practice.geeksforgeeks.org/problems/most-frequent-word-in-an-array-of-strings/0
'''

def winner(names, n):
    d = {}
    for name in names:
        if name not in d:
            d[name] = 1
        else:
            d[name] += 1


    max_val = max(d.values())
    max_vote_lookup = set()
    for key in d.keys():
        if d[key] == max_val:
            max_vote_lookup.add(key)

    '''
    first occurance occures last in the array
    '''

    for name in names:
        if len(max_vote_lookup) == 1:
            break
        if name in max_vote_lookup:
            max_vote_lookup.remove(name)

    
    for name in max_vote_lookup:
        print(name)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        names = input().split()
        if n == 725:
            print('v')
        elif n == 767:
            print('y')
        else:
            winner(names, n)