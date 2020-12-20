# coding: UTF-8
# 最长公共前缀


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(str1, str2):
            result = ''
            length = min(len(str1), len(str2))
            for idx in range(length):
                if str1[idx] == str2[idx]:
                    result += str1[idx]
                else:
                    break
            return result
        if not strs:
            return ''
        else:
            prefix = strs[0]
            for i in strs:
                prefix = lcp(prefix, i)
                if not prefix:
                    break
            return prefix

