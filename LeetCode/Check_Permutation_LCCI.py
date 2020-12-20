# coding: UTF-8
# 判断str2 是不是 str1 的重排


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        dict1 = {}
        dict2 = {}
        for i in s1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in s2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1

        for j in dict1:
            if j not in dict2:
                return False
            elif dict1[j] != dict2[j]:
                return False
        return True


s = Solution()
print(s.CheckPermutation('abc', 'bad'))
