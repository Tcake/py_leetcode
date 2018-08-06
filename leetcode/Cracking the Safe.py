class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        max = k ** n
        cache = {}
        self.result_str = '0' * (n - 1)
        begin = self.result_str

        def slave(target):
            if target == begin and len(cache) == max:
                return True
            for i in range(k):
                new_road = target + str(i)
                if not cache.get(new_road):
                    cache.update({new_road: True})
                    self.result_str += str(i)
                    res = slave(new_road[1:])
                    if res:
                        return True
                    self.result_str = self.result_str[: -1]
                    cache.pop(new_road)
            return False

        slave(self.result_str)
        return self.result_str


# class Solution:
#     def crackSafe(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: str
#         """
#         ans = "0" * (n - 1)
#         visits = set()
#         for x in range(k ** n):
#             current = ans[-n+1:] if n > 1 else ''
#             for y in range(k - 1, -1, -1):
#                 if current + str(y) not in visits:
#                     visits.add(current + str(y))
#                     ans += str(y)
#                     break
#         return ans


a = Solution()
print(a.crackSafe(2,3))

