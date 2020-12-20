# coding:UTF-8
# 求两个单词之间的最短编辑距离


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        if n * m == 0:
            return n + m
        # 初始化
        dp = [[0] * (m+1) for _ in range(n+1)]

        # 边界状态
        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, m+1):
            dp[0][j] = j
        print(dp)
        # 动态推导
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    # print(word1[i-1])
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        print(dp)
        return dp[n][m]


s = Solution()

s.minDistance('hor', 'r')
