'''
https://practice.geeksforgeeks.org/problems/trie-insert-and-search/0
'''


class Node:
    def __init__(self, val):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children.get(char)
        current.end_of_word = True


    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children.get(char)
        return current.end_of_word

if __name__ == '__main__':
    for _ in range(int(input())):
        trie = Trie()
        n = int(input())
        strings = input().split()
        for string in strings:
            trie.insert(string)
        to_find = input()
        ans = trie.search(to_find)
        if ans:
            print(1)
        else:
            print(0)
