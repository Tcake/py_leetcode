class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 1
        row = len(dungeon)
        col = len(dungeon[0])
        dp = [[0]*col for _ in range(row)]
        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)
        for j in range(col - 2, -1, -1):
            dp[-1][j] = max(dp[-1][j + 1] - dungeon[-1][j], 1)

        for i in range(row - 2, -1, -1):
            dp[i][-1] = max(dp[i + 1][-1] - dungeon[i][-1], 1)
            for j in range(col - 2, -1, -1):
                right = max(dp[i][j + 1] - dungeon[i][j], 1)
                down = max(dp[i + 1][j] - dungeon[i][j], 1)
                dp[i][j] = min(right, down)

        return dp[0][0]


# class Solution:
#     def calculateMinimumHP(self, dungeon):
#         """
#         :type dungeon: List[List[int]]
#         :rtype: int
#         """
#         if not dungeon or not dungeon[0]:
#             return 1
#
#         m, n = len(dungeon), len(dungeon[0])
#
#         dp = [[2 ** 32 - 1] * (n + 1) for _ in range(m + 1)]
#         dp[m - 1][n] = 1
#         dp[m][n - 1] = 1
#
#         for i in range(m - 1, -1, -1):
#             for j in range(n - 1, -1, -1):
#                 tmp = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
#                 if tmp <= 0:
#                     tmp = 1
#                 dp[i][j] = tmp
#
#         return dp[0][0]

a = Solution()
test = [[-2,-3,3],
        [-5,-10,1],
        [10,30,-5]]
print(a.calculateMinimumHP(test))
