class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0] * len(s) for _ in range(len(s))]
        return self.robot(s, dp, 0, len(s) - 1)

    def robot(self, s, dp, i, j):
        if s == '':
            return 0
        if i == j:
            return 1
        if i > j:
            return 0

        if dp[i][j]:
            return dp[i][j]

        dp[i][j] = self.robot(s, dp, i + 1, j) + 1

        for k in range(i + 1, j + 1):
            if s[k] == s[i]:
                dp[i][j] = min(dp[i][j], self.robot(s, dp, i, k - 1) + self.robot(s, dp, k + 1, j))
        return dp[i][j]


# class Solution:
#     def strangePrinter(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         l = len(s)
#         path = [[0 for j in range(l)] for i in range(l)]
#
#         def solve(i, j):
#             if i > j: return 0
#             if path[i][j] > 0: return path[i][j]
#             ans = solve(i, j - 1) + 1
#
#             for k in range(i, j):
#                 if s[k] == s[j]:
#                     ans = min(ans, solve(i, k) + solve(k + 1, j - 1))
#             path[i][j] = ans
#             return ans
#
#         return solve(0, l - 1)

a = Solution()
test = 'aba'
print(a.strangePrinter(test))