'''
class Node{
    map <character, Node> children;
}

map means dictionary
its key will be character and value will be Node
key = character
value = Node

Resources 

https://www.youtube.com/watch?v=AXjmTQ8LEoI
https://leetcode.com/problems/implement-trie-prefix-tree/discuss/314763/Python-Solution-w-Node-and-map
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


    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children.get(char)
        return True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children.get(char)
        return current.end_of_word

    def delete(self, word):
        current = self.root
        self.delete_(current, word)

    def delete_(self, current, word):
        pass 

