"""
Link: https://leetcode.com/problems/lru-cache/

utilize a doubly linked list and hashmap. The reason for this is because we have to keep track of the cache keys that we use and be able to manipulate the key value pairs. We also need to be able to remove an element should it go over capacity and the only thing that lets us do that in O(1) time is these data structures.

{
    1: node.val = 2
    2: node.val = 7
    3: node.val = 6
}

1. make and instantiate a node class. with two dummy nodes to act as a left and right node to connect to eachother. Instantiate a hashmap. 

2. remove() key:value pair in cache + LL
    2a. insert() it back in the front of the cache and LL
    2b. if key is not in the map then return -1

3. 
"""

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int): # is the size of the array
        self.cap = capacity
        self.cache = {}
        self.old = Node(0,0)
        self.latest = Node(0,0)

        self.old.next = self.latest
        self.latest.prev = self.old

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.latest.prev, self.latest
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev 

    def get(self, key: int) -> int: #return the key if exists or -1
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else: 
            return -1
 
    def put(self, key: int, value: int) -> None: #updates value of the key if exists else add key-value pair if # of keys exceeds capacity remove LRU key
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        lru = self.old.next
        if len(self.cache) > self.cap:
            self.remove(lru)
            del self.cache[lru.key]            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
