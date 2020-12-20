# coding：UTF-8
# 最小路径和


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, columns):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1, rows):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        for m in range(1, rows):
            for n in range(1, columns):
                dp[m][n] = min(dp[m-1][n] + grid[m][n], dp[m][n-1] + grid[m][n])
        return dp[-1][-1]
