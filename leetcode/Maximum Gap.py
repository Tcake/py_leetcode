class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_nums = len(nums)
        if l_nums < 2:
            return 0

        nums.sort()
        result = 0
        for i in range(1, l_nums):
            tmp = nums[i] - nums[i - 1]
            result = max(tmp, result)

        return result


a = Solution()
test = [3,6,9,1]
print(a.maximumGap(test))