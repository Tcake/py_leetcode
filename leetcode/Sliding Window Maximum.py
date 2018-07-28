class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return []
        target_max = max(nums[:k])
        result = [target_max,]
        for i in range(k, len(nums)):
            if nums[i] >= target_max:
                target_max = nums[i]
            else:
                if nums[i-k] == target_max:
                    target_max = max(nums[i-k+1: i+1])
            result.append(target_max)
        return result


a = Solution()
test =[1,3,-1,-3,5,3,6,7]
print(a.maxSlidingWindow(test,3))
