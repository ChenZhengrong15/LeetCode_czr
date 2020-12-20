# coding:UTF-8
# 左上角到右下角的不同路径数


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0] * n for _ in range(m)]
        dp = [[1] * n for _ in range(m)]
        # dp[0][0] = 1
        # for i in range(1, m):
        #     dp[i][0] = dp[i-1][0]
        # for j in range(1, n):
        #     dp[0][j] = dp[0][j-1]
        for l in range(1, m):
            for k in range(1, n):
                dp[l][k] = dp[l][k-1] + dp[l-1][k]

        return dp[-1][-1]



