# coding: UTF-8
# 滑动窗口思想
# https://leetcode-cn.com/problems/minimum-window-substring/solution/zui-xiao-fu-gai-zi-chuan-by-leetcode-solution/

from collections import defaultdict
from collections import Counter


class Solution:  # overtime
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        ans = ''
        length = m
        lk, rk = 0, 1
        while rk <= m:  # 注意等号，rk是可以取值到 m 的
            # print(lk, rk)
            if self.is_contain(s[lk: rk], t):
                if length >= rk - lk:  # 注意等号，相等的时候也说明存在覆盖
                    ans = s[lk: rk]
                    length = rk - lk
                lk += 1
            else:
                rk += 1
        return ans

    def is_cover(self, str1: str, str2: str):
        # 判断 str1 是否完全覆盖 str2
        dict1 = dict()
        dict2 = dict()

        for i in str1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in str2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        for i in str2:
            if i not in dict1 or dict1[i] < dict2[i]:
                return False
        return True

    def is_contain(self, str1, str2):
        target = Counter(str2)
        counter = defaultdict(int)
        for i in str1:
            if i in str2:
                counter[i] += 1
        if len(counter) < len(target):
            return False
        for k in target:
            if k not in counter or counter[k] < target[k]:
                return False
        return True


s = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(s.minWindow(S, T))

#
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#
#         for i in t:
#             if i in need:
#                 need[i] += 1


