# coding:UTF-8
# 判断给定字符串是否能结尾给定wordDict中的单词


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(length):
            for j in range(i+1, length+1):
                if dp[i] and s[i: j] in wordDict:
                    dp[j] = True
        return dp[-1]
