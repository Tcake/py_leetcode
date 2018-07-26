class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return 0
        result = 0
        row_n = len(grid)
        col_n = len(grid[0])
        row_max = [0] * row_n
        col_max = [0] * col_n
        for i in range(row_n):
            for j in range(col_n):
                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])
        for i in range(row_n):
            for j in range(col_n):
                result += min(row_max[i], col_max[j]) - grid[i][j]
        return result


a = Solution()
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(a.maxIncreaseKeepingSkyline(grid))


# class Solution(object):
#     def maxIncreaseKeepingSkyline(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         max_h = [max(line) for line in grid]
#         max_v = [max(line) for line in zip(*grid)]
#         ans = [min(max_h[i], max_v[j]) - grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))]
#         return sum(ans)
