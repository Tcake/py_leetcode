from time import sleep, time

class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        init_pool = []
        for i in range(maxChoosableInteger):
            init_pool.append(i + 1)
        cache = {}

        def salve(pool, nowtotal):

            if pool[-1] >= nowtotal:
                return True

            tmp = pool[:]
            for i in range(len(tmp)):

                nowtotal -= tmp[i]

                flag = True
                tmp_two = tmp[: i] + tmp[i + 1:]
                if nowtotal <= tmp_two[-1]:
                    return False
                for j in range(len(tmp_two)):
                    hash = str(tmp_two[: j] + tmp_two[j + 1:])
                    if hash in cache:
                        res = cache[hash]
                    else:
                        res = salve(tmp_two[: j] + tmp_two[j + 1:], nowtotal - tmp_two[j])
                        cache[hash] = res
                    if not res:
                        flag = False
                        break
                nowtotal += tmp[i]
                if flag:
                    return True

            return False

        return salve(init_pool, desiredTotal)

    # def canIWin(self, maxChoosableInteger, desiredTotal):
    #     """
    #     :type maxChoosableInteger: int
    #     :type desiredTotal: int
    #     :rtype: bool
    #     """
    #     if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
    #         return False
    #     self.memo = {}
    #
    #     return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)
    #
    # def helper(self, nums, desiredTotal):
    #
    #     hash = str(nums)
    #     if hash in self.memo:
    #         return self.memo[hash]
    #
    #     if nums[-1] >= desiredTotal:
    #         return True
    #
    #     for i in range(len(nums)):
    #         if not self.helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i]):
    #             self.memo[hash] = True
    #             return True
    #     self.memo[hash] = False
    #     return False



# class Solution1:
#     def canIWin(self, choose, total):
#         """
#         :type choose: int
#         :type total: int
#         :rtype: bool
#         """
#         if choose*(choose+1)/2<total: return False
#         memo = {}
#
#         def dp(cur, used):
#             print(cur, used)
#             if used in memo:
#                 return memo[used]
#             else:
#                 for i in range(choose, 0, -1):
#                     if not used & (1 << i):
                        #todo:这里使用了二进制异或原理来标记数值是否被使用过，想象力非凡！！！
#                         if cur+i >= total:
#                             memo[used] = True
#                             return True
#                         if not dp(cur+i, used | (1 << i)):
#                             memo[used] = True
#                             return True
#                 memo[used] = False
#                 return False
#         return dp(0, 0)


s = time()
a = Solution()
print(a.canIWin(18,79))
print(time() - s)


