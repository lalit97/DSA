'''
understanding the problem
https://www.youtube.com/watch?v=S6IfqDXWa10

https://leetcode.com/problems/lru-cache/discuss/352295/Python3-doubly-linked-list-and-dictionary

https://leetcode.com/problems/lru-cache/discuss/46171/Clean-python-code-with-Doubly-Linked-List-%2B-HashTable
'''

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(0, 0)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def get(self, key):
        if key in self.cache:
            node = self.cache.get(key)
            self.remove_from_list(node)
            self.insert_into_head(node)
            return node.val
        return -1


    def set(self, key, value):
        if key in self.cache:
            node = self.cache.get(key)
            self.remove_from_list(node)
            self.insert_into_head(node)
            node.val = value  # update value 
        else:
            if len(self.cache) >= self.capacity:
                self.remove_from_tail()
            node = Node(key, value)
            self.cache[key] = node
            self.insert_into_head(node)


    def remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_into_head(self, node):
        next_to_head = self.head.next
        self.head.next = node
        node.next = next_to_head
        node.prev = self.head
        next_to_head.prev = node


    def remove_from_tail(self):
        if len(self.cache) == 0:
            return
        tail_node = self.tail.prev
        del self.cache[tail_node.key]
        self.remove_from_list(tail_node)
