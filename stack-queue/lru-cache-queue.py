'''
understanding the problem
https://www.youtube.com/watch?v=S6IfqDXWa10

using deque
https://leetcode.com/problems/lru-cache/discuss/46221/Share-my-two-Python-solutions


'''
from collections import deque


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.order = deque()
        
        
    def get(self, key):
        if key in self.cache:
            value = self.cache.get(key)
            self.order.remove(key)
            self.order.append(key)
            return value
        return -1


    def set(self, key, value):
        '''
        set key value in your cache
        '''
        if key in self.cache:
            self.order.remove(key)
        self.cache[key] = value
        self.order.append(key)

        if len(self.cache) > self.capacity:
            oldest = self.order.popleft()
            del self.cache[oldest]