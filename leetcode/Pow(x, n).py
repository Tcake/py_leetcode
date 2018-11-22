class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            tmp = 1 / x
            n = abs(n)
        else:
            tmp = x
        res = 1
        while n:
            if n & 1:
                res *= tmp
            n >>= 1
            tmp **= 2

        return res


print(Solution().myPow(2,-2))
