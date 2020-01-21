'''
https://practice.geeksforgeeks.org/problems/winner-of-an-election-where-votes-are-represented-as-candidate-names/0
'''



def winner(names, n):
    d = {}
    for name in names:
        if name not in d:
            d[name] = 1
        else:
            d[name] += 1

    max_val = max(d.values())

    candidates_with_max_votes = []
    for key in d.keys():
        if d[key] == max_val:
            candidates_with_max_votes.append(key)
    sort_by_name = sorted(candidates_with_max_votes)
    winner = sort_by_name[0]

    print(winner, max_val)


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        names = input().split()
        winner(names, n)