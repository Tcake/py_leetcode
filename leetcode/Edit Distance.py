class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word2 and not word1:
            return 0
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 2)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:

                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, min(dp[i][j - 1] + 1, dp[i - 1][j] + 1))
        return dp[m][n]


a = Solution()
print(a.minDistance('', 'a'))


# class Solution(object):
#     def minDistance(self, word1, word2):
#         l1, l2 = len(word1)+1, len(word2)+1
#
#         pre = [i for i in range(l2)]
#
#         for i in range(1, l1):
#             cur = [i]*l2
#             for j in range(1, l2):
#                 cur[j] = min(cur[j-1]+1, pre[j]+1, pre[j-1]+(word1[i-1]!=word2[j-1]))
#             pre = cur[:]
#         return pre[-1]
