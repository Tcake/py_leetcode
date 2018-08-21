class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 1
        elif n > 10:
            n = 10

        def salve(step):
            if step == 1:
                return 10
            total = 9
            for i in range(9, 9 - step + 1, -1):
                total *= i
            return total + salve(step - 1)

        return salve(n)


a = Solution()
print(a.countNumbersWithUniqueDigits(10))
