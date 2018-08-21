class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}

        def salve(step):
            if step == 0 or step == 1:
                return 1
            if step in cache:
                return cache[step]
            else:
                cache[step] = salve(step - 1) + salve(step - 2)
                return cache[step]

        return salve(n)


a = Solution()
print(a.climbStairs(35))
