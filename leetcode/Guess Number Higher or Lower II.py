class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        result = 0
        while right - left >= 6:
            left = (right + left) // 2
            result += left

        if left is not 1:
            left += 1
        tmp = right - left
        if tmp == 1:
            result += left
        elif tmp == 2:
            result += left + 1
        elif tmp == 3:
            result += left * 2 + 2
        elif tmp == 4:
            result += left * 2 + 4
        elif tmp == 5:
            result += left * 2 + 6

        return result


a = Solution()
print(a.getMoneyAmount(7))
