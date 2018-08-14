class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cache = [0] * n
        cache[-1] = 1
        for i in range(m):
            for j in range(n - 2, -1, -1):
                cache[j] += cache[j + 1]
        return cache[0]

a = Solution()
print(a.uniquePaths(7,3))