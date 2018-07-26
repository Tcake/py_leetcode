class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 0
        if divisor < 0:
            flag += 1
            divisor = - divisor
        if dividend < 0:
            flag += 1
            dividend = - dividend
        result = self.slave(dividend, divisor)
        if flag == 1:
            result = - result
        if result < - 2**31 or result > 2**31 - 1:
            return 2**31 - 1
        return result

    def slave(self, dividend, divisor):
        if dividend < divisor:
            return 0
        count = 1
        div = divisor
        while dividend > div + div:
            div += div
            count += count
        return count + self.slave(dividend - div, divisor)


a = Solution()
print(a.divide(10, 3))
