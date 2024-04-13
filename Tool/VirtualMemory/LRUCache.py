class Node:
    def __init__(self,key=None, data=None):
        self.key, self.data = key, data
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity=None):
        self.capacity=capacity
        self.cache = {}

        #left=LRU
        #right=most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            #insert at the right as most recently used
            self.insert(self.cache[key])
            return self.cache[key].data

        return -1
    
    def put(self, key, data):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, data)
        self.insert(self.cache[key])

        if (len(self.cache) > self.capacity):
            # remove and delete LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def get_current_cache(self):
        cache_as_list = []
        for key, data in self.cache.items():
            cache_as_list .append(key)

        if (len(cache_as_list) < self.capacity):
            for i in range(self.capacity - len(cache_as_list)):
                cache_as_list.append(-1)

        print(cache_as_list)
        return cache_as_list 
