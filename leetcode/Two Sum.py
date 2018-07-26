class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        tmp = nums[:]
        tmp.sort()
        while left < right:
            if tmp[left] + tmp[right] < target:
                left += 1
            elif tmp[left] + tmp[right] > target:
                right -= 1
            else:
                index_le = nums.index(tmp[left])
                index_right = nums.index(tmp[right])
                if index_le > index_right:
                    return [index_right, index_le]
                elif index_le == index_right:
                    nums = nums[index_le + 1:]
                    index_right = nums.index(tmp[right])
                    return [index_le, index_right + index_le + 1]
                else:
                    return [index_le, index_right]
        return None


a = Solution().twoSum([3, 2, 2, 3], 6)
print (a)
