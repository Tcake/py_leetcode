class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nlen = len(nums)
        target = 1
        cache = {}
        for i in range(nlen):
            if nums[i] == target:
                target += 1
                while True:
                    tmp = cache.get(target, False)
                    if tmp:
                        target += 1
                    else:
                        break
            else:
                cache.update({nums[i]: True})
        return target


a = Solution()
test = [1,2,3,7,8,9,11,12]
print(a.firstMissingPositive(test))