class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        mid = l // 2 + 1

        tmp = []
        i1 = i2 = 0
        for i in range(mid):
            if i1 == len(nums1):
                tmp.append(nums2[i2])
                i2 += 1

            elif i2 == len(nums2):
                tmp.append(nums1[i1])
                i1 +=1

            elif nums1[i1] <= nums2[i2]:
                tmp.append(nums1[i1])
                i1 += 1

            else:
                tmp.append(nums2[i2])
                i2 += 1

        if l % 2 == 0:
            res = (tmp[-1]+ tmp[-2]) / 2
        else:
            res = tmp[-1]

        return res

a = [1,2]
b = [3, 4]
print (Solution().findMedianSortedArrays(a,b))