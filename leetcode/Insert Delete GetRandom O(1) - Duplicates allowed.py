from random import choice


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}
        self.list = []
        self.len_list = -1

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.list.append(val)
        self.len_list += 1
        if val not in self.cache:
            self.cache[val] = [self.len_list]
            return True
        else:
            self.cache[val].append(self.len_list)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.cache:
            return False
        else:
            index = self.cache[val].pop()
            if not self.cache[val]:
                self.cache.pop(val)
            self.list[index] = None
            return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        while True:
            res = choice(self.list)
            if res is not None:
                return res


# class RandomizedCollection:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hash_table = {}
#         self.value = []
#
#     def insert(self, val):
#         """
#         Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
#         :type val: int
#         :rtype: bool
#         """
#         result = None
#         if val in self.hash_table:
#             self.hash_table[val].add(len(self.value))
#             result = False
#         else:
#             self.hash_table[val] = set([])
#             self.hash_table[val].add(len(self.value))
#             result = True
#         self.value.append(val)
#         return result
#
#     def remove(self, val):
#         """
#         Removes a value from the collection. Returns true if the collection contained the specified element.
#         :type val: int
#         :rtype: bool
#         """
#         if val not in self.hash_table:
#             return False
#         else:
#             index = self.hash_table[val].pop()
#             last = self.value[-1]
#             self.value[index] = last
#             self.hash_table[last].add(index)
#             self.hash_table[last].discard(len(self.value) - 1)
#             self.value.pop()
#             if len(self.hash_table[val]) == 0:
#                 self.hash_table.pop(val, 0)
#             return True
#
#     def getRandom(self):
#         """
#         Get a random element from the collection.
#         :rtype: int
#         """
#         return self.value[random.randint(0, len(self.value) - 1)]