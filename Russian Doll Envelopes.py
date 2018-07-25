class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes = sorted(envelopes, cmp=lambda x, y: self.cmp_envelopes(x, y))
        result = self.max_count_enelopes(zip(*envelopes)[1])
        return result

    def cmp_envelopes(self, a, b):
        if a[0] > b[0]:
            return 1
        elif a[0] < b[0]:
            return -1
        else:
            if a[1] >= b[1]:
                return -1
            else:
                return 1

    def max_count_enelopes(self, nums):
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)


a = Solution()
test = [[5,4],[5,4],[5,7],[2,3]]
print(a.maxEnvelopes(test))

# class Solution(object):
#     def maxEnvelopes(self, envelopes):
#         nums = sorted(envelopes, key=lambda x: (x[0], -x[1]))
#         tails = [0] * len(nums)  # 寻找最长递增子序列
#         upper = 0
#         for ele in nums:
#             pos = bisect.bisect_left(tails, ele[1], 0, upper)  # 找到插入位置或者原理位置
#             tails[pos] = ele[1]  # 更新数据
#             if pos == upper:  # 如果当前
#                 upper += 1
#         return upper
