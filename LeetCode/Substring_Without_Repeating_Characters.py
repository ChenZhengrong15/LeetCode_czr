# coding:UTF-8
# 最常无重复字符的子串
# 动态规划 超时
# 滑动窗口算法，利用哈希集合的无重复特性帮助找到各起始位置的最长无重复字符串 ac


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        # 边界条件
        for i in range(length):
            dp[i][i] = True

        # 推导
        for i in range(length-1):
            for j in range(i+1, length):
                if s[j] in s[i: j]:
                    dp[i][j] = False
                else:
                    dp[i][j] = True and dp[i][j-1]
        # print(dp)
        ans = 0
        for i in range(length):
            for j in range(i, length):
                if dp[i][j] is True and j - i > ans:
                    ans = j - i
                    # print(s[i: j+1])
        return ans + 1


s = Solution()
print(s.lengthOfLongestSubstring('Notice that the answer must be a substring, "pwke" is a subsequence and not a substring'))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        occ = set()
        ans, rk = 0, -1  # rk 右指针
        for i in range(n): # i 就是左指针
            if i != 0:
                occ.remove(s[i-1])
            while rk + 1 < n and s[rk+1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk-i+1)  # 不断更新 ans 的值，记录了第i个字符起的最长无重复子串的长度
        return ans

