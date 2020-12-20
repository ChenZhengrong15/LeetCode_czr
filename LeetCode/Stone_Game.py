# # coding: UTF-8
# 石子游戏,先手必胜
# 动态规划 dp[i][j] 表示剩余石堆下标是 i 到 j 之间时，先手石子多余后手的数量


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        # 初始化
        dp = [[0] * length for _ in range(length)]
        # 边界条件
        for i in range(length):
            dp[i][i] = piles[i]
        # 动态推导
        for i in range(length-2, -1, -1):
            for j in range(i+1, length):
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][length-1] > 0
