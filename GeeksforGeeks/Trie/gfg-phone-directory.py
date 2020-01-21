'''
https://practice.geeksforgeeks.org/problems/phone-directory/0

help
https://www.geeksforgeeks.org/auto-complete-feature-using-trie/
'''
class Node:
    def __init__(self, val):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node('')
        self.suggestions = []


    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children.get(char)
        current.end_of_word = True


    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children.get(char)
        return True


    def print_suggestions(self, prefix):
        current = self.root
        temp_word = ''
        for char in prefix:
            temp_word += char
            current = current.children.get(char)
        # till now we have reached till the pattern   

        self.print_recursive(current, temp_word)

        sorted_suggestions = sorted(self.suggestions)
        for sugg in sorted_suggestions:
            print(sugg, end=' ')
        print()
        # clearing for next query
        self.suggestions = []


    def print_recursive(self, current, word):
        if current.end_of_word:
            self.suggestions.append(word)

        for char, node in current.children.items():
            self.print_recursive(node, word+char)


if __name__ == '__main__':
    for _ in range(int(input())):
        trie = Trie()
        n = int(input())
        names = input().split()

        for name in names:
            trie.insert(name)

        query = input()
        len_q = len(query)

        for i in range(1, len_q+1):
            pat = query[:i]
            if trie.starts_with(pat):  # if the pattern is present in trie
                trie.print_suggestions(pat)
            else:
                print(0)