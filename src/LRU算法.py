# 解题思路
    # 哈希表 + 链表

class LRU:

    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.used_list = []


    def get(self,key):
        if key in self.cache:
            # 移动到最近使用的位置
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


# 通义大模型版本
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.used_list = []

    def get(self, key: int) -> int:
        if key in self.cache:
            # 移动到最近使用的位置
            self.used_list.remove(key)
            self.used_list.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 更新已有键值对，并移动到最近使用的位置
            self.used_list.remove(key)
        elif len(self.cache) == self.capacity:
            # 缓存满时移除最久未使用的键
            oldest_key = self.used_list.pop(0)
            del self.cache[oldest_key]
        
        # 插入或更新键值对
        self.used_list.append(key)
        self.cache[key] = value

# 该数据结构需要满足
# 1.支持从数组尾部插入元素 2. 支持从数组头部去除元素 3.支持将数组中的任意元素插入到尾部，都需要o(1)的时间复杂度
# 考虑使用哈希表加双向链表

class Node:

    def __init__(self,key=None,value=None) -> None:
        self.key = key
        self.value = value

        # 前指针与后指针
        self.pre = None
        self.next = None


class LRU:

    def __init__(self,cap) -> None:
        self.cap = cap
        self.hash_map = {}

        # 加入头部与尾部节点
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.pre = self.head


    def move_node_to_tail(self,key):

        node = self.hash_map[key]

        # 从数据结构中取出node
        node.pre.next = node.next
        node.next.pre = node.pre

        # 将node放入到数据结构尾部
        node.next = self.tail
        node.pre = self.tail.pre

        self.tail.pre.next = node
        self.tail.pre = node

    def get(self,key):
        if key in self.hash_map:
            # 如果已经在链表中了久把它移到末尾（变成最新访问的）
            self.move_node_to_tail(key)
            return self.hash_map[key].value
        else:
            return -1


    def put(self,key,value):
        if key in self.hash_map:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的value
            self.hash_map[key].value = value
            # 之后将该节点移到末尾
            self.move_node_to_tail(key)

        else:
            if len(self.hash_map) == self.cap:
                # 去掉哈希表对应项
                node = self.hash_map.pop(self.head.next.key)
                # 去掉最久没有被访问过的节点，即头节点之后的节点
                self.head.next = node.next
                node.next.pre = self.head

            # 如果不在的话就插入到尾节点前
            new_node = Node(key,value)
            self.hash_map[key] = new_node

            new_node.next = self.tail
            new_node.pre = self.tail.pre

            self.tail.pre.next = new_node
            self.tail.pre = new_node