from time import sleep
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        def salve(iterm):
            print(cache)
            # sleep(0.5)
            is_cache = cache.get(str(iterm))
            if is_cache is not None:
                return is_cache
            if not iterm:
                return 0
            if len(iterm) == 1:
                return iterm[0]

            result = max(iterm[0] + salve(iterm[2:]), iterm[1] + salve(iterm[3:]))
            cache.update({str(iterm): result})

            return result

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(nums[0] + salve(nums[2:-1]), nums[1] + salve(nums[3:]), salve(nums[2:]))


a = Solution()
test = [2,3,4]
test1 = [155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]
test2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
test3 = [0,0,0,0,0]
print(a.rob(test2))
