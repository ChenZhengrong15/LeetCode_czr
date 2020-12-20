# coding: UTF-8
# 最长回文子串


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(st, l, r):
            while l >= 0 and r < len(st) and st[l] == st[r]:
                l -= 1
                r += 1
            return l+1, r-1

        start, end = 0, 0
        length = len(s)
        for i in range(length):
            left1, right1 = helper(s, i, i+1)
            left2, right2 = helper(s, i, i)
            # print(left1, right1, left2, right2)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        # print(start, end)
        return s[start: end+1]



class Solution1:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        # 初始化
        dp = [[False] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
        # 边界条件
        for i in range(length-1):
            dp[i][i+1] = (s[i] == s[i+1])
        # 动态推导
        for l in range(2, length):
            for i in range(length):
                j = i + l
                if j >= length:
                    break
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        start, end = 0, 0
        for i in range(length):
            for j in range(i, length):
                if (dp[i][j] is True) and (j - i > end - start):
                    start, end = i, j
        return s[start: end+1]

s =Solution1()
a = s.longestPalindrome('ababa')
print(a)

