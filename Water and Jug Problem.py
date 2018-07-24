class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x > y:
            x, y = y, x
        if x == 0:
            if z == y or z == x:
                return True
            else:
                return False
        for i in range(1, x + 1):
            if (y % i) == 0 and (x % i) == 0:
                com_divisor = i
        return self.main(x, y, z, com_divisor)

    def main(self, x, y, z, com_divisor):
        if z <= x:
            if z == x:
                return True
            elif z % com_divisor == 0:
                return True
            else:
                return False
        elif x < z <= y:
            if z == y:
                return True
            else:
                return self.main(x, y, z % x, com_divisor)
        else:
            if z == (x + y):
                return True
            elif z < (x + y):
                return self.main(x, y, z - y, com_divisor)
            else:
                return False


a = Solution().canMeasureWater(13, 11, 1)
print(a)


# class Solution(object):
#     def canMeasureWater(self, x, y, z):
#         """
#         :type x: int
#         :type y: int
#         :type z: int
#         :rtype: bool
#         """
#         if x > y: x, y = y, x
#         gcd = self.gcd(x, y)
#         if gcd == 0: return z == 0
#         return z % gcd == 0 and z <= x + y
#
#     def gcd(self, a, b):
#         if a == 0: return b
#         return self.gcd(b % a, a)
