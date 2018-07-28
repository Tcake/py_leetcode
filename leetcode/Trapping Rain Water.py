class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        list_len = len(height)
        left_max = []
        right_max = []
        max_l = 0
        max_r = 0
        for i in range(list_len):
            if height[i] > max_l:
                max_l = height[i]
            left_max.append(max_l)
            if height[list_len - i - 1] > max_r:
                max_r = height[list_len - i - 1]
            right_max.insert(0, max_r)
        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(list_len))


a = Solution()
test = [0,1,0,2,1,0,1,3,2,1,2,1]
print(a.trap(test))


# class Solution:
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#
#         if len(height) is 0:
#             return 0
#
#         left = 0
#         right = len(height) - 1
#         leftmax = 0
#         rightmax = 0
#
#         watersum = 0
#
#         while left < right:
#             if height[left] < height[right]:
#                 if height[left] > leftmax:
#                     leftmax = height[left]
#                 else:
#                     watersum += leftmax - height[left]
#                 left += 1
#             else:
#                 if height[right] > rightmax:
#                     rightmax = height[right]
#                 else:
#                     watersum += rightmax - height[right]
#                 right -= 1
#
#         return watersum
