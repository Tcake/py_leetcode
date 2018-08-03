class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.len = 0
        self.queue = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cache.get(key):
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print(self.cache)
        print(self.queue)
        is_exist = self.get(key)
        if is_exist != -1:
            self.cache.update({key: value})
            return
        if self.len == self.capacity:
            tmp = self.queue.pop(0)
            self.cache.pop(tmp)
        else:
            self.len += 1

        self.queue.append(key)
        self.cache.update({key: value})


cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
print(cache.get(2))
cache.put(1, 1)
# print(cache.get(2))
cache.put(4, 1)
# print(cache.get(1))
# print(cache.get(3))
print(cache.get(2))

# 最优解法是使用双向链表
# class _LRUCacheNode:
#
#     def __init__(self, key, value):
#         self.key = key
#         self.val = value
#         self.next = None
#         self.prev = None
#
#
# class LRUCache:
#
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.mapping = {}
#         # create two dummy node
#         self.head = _LRUCacheNode('head', None)
#         self.tail = _LRUCacheNode('tail', None)
#         # connect head and tail
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self.mapping:
#             return -1
#
#         node = self.mapping[key]
#         self.__move_to_head(key)
#         return node.val
#
#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         # remove node when cache is full
#         if self.capacity == len(self.mapping) and key not in self.mapping:
#             old_tail = self.tail.prev
#             prev = old_tail.prev
#             # connect tail and prev one of the old_tail
#             self.tail.prev = prev
#             prev.next = self.tail
#             # remove to old tail
#             self.mapping.pop(old_tail.key)
#         # insert new node
#         if key not in self.mapping:
#             node = _LRUCacheNode(key, value)
#             self.mapping[key] = node
#             old_head = self.head.next
#             self.head.next = node
#             node.prev = self.head
#             node.next = old_head
#             old_head.prev = node
#         else:
#             self.__move_to_head(key)
#         # update value
#         self.mapping[key].val = value
#
#     def __move_to_head(self, key):
#         """
#         :type key: int
#         :type value: int
#         """
#         node = self.mapping[key]
#         next, prev = node.next, node.prev
#
#         # connect the next one and the prev one
#         next.prev = prev
#         prev.next = next
#
#         # move the node to head
#         old_head = self.head.next
#         self.head.next = node
#         node.prev = self.head
#         node.next = old_head
#         old_head.prev = node