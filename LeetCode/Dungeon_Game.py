# coding: UTF-8
# 地下城游戏 骑士-> 哥公主


# class Solution:
#     # def calculateMinimumHP(self, dungeon) -> int:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         m = len(dungeon)
#         n = len(dungeon[0])
#
#         # 初始化
#         dp_state = [[0] * n for _ in range(m)]
#         dp_lowest = [[0] * n for _ in range(m)]
#
#         # 边界条件
#         dp_state[0][0] = dungeon[0][0]
#         dp_lowest[0][0] = dungeon[0][0]
#
#         for i in range(1, n):
#             dp_state[0][i] = dp_state[0][i-1] + dungeon[0][i]
#             dp_lowest[0][i] = min(dp_state[0][i], dp_lowest[0][i-1])
#
#         for i in range(1, m):
#             dp_state[i][0] = dp_state[i-1][0] + dungeon[i][0]
#             dp_lowest[i][0] = min(dp_state[i][0], dp_lowest[i-1][0])
#
#         for i in range(1, m):
#             for j in range(1, n):
#                 if dp_lowest[i][j - 1] > dp_lowest[i - 1][j]:
#                     dp_state[i][j] = dp_state[i][j - 1] + dungeon[i][j]
#                     dp_lowest[i][j] = min(dp_lowest[i][j - 1], dp_state[i][j])
#                 elif dp_lowest[i][j - 1] > dp_lowest[i - 1][j]:
#                     dp_state[i][j] = dp_state[i - 1][j] + dungeon[i][j]
#                     dp_lowest[i][j] = min(dp_lowest[i - 1][j], dp_state[i][j])
#                 else:
#                     if dp_state[i][j - 1] > dp_state[i - 1][j]:
#                         dp_state[i][j] = dp_state[i][j - 1] + dungeon[i][j]
#                         dp_lowest[i][j] = min(dp_lowest[i][j - 1], dp_state[i][j])
#                     else:
#                         dp_state[i][j] = dp_state[i - 1][j] + dungeon[i][j]
#                         dp_lowest[i][j] = min(dp_lowest[i - 1][j], dp_state[i][j])
#         if dp_lowest[-1][-1] <= 0:
#             return 1 + abs(dp_lowest[-1][-1])
#         else:
#             return 1


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        BIG = 10 ** 9
        dp = [[BIG] * (m+1) for _ in range(n+1)]
        dp[n][m-1] = dp[n-1][m] = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)

        return dp[0][0]
