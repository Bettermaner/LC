# 解题思路
    # 哈希表 + 链表

class LRU:

    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.used_list = []


    def get(self,key):
        if key in self.cache:
            if key != self.used_list[-1]:
                self.used_list.remove(key)
                self.used_list.append(key)
                return self.cache[key]
        else:
            return -1

    def put(self,key,value):
        if key in self.cache:
            self.used_list.remove(key)

        elif len(self.cache) == self.capacity:
            oldest_key = self.used_list.pop(0)
            self.cache.pop(oldest_key)
            
        self.used_list.append(key)
        self.cache[key] = value