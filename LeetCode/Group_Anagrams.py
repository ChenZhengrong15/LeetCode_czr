# coding: UTF-8
# 字母异位词
# 排序字符串相等时是同一类
# HashMapFunc 优化


class Solution1:  # overtime
    def groupAnagrams(self, strs):
        def helper(word1: str, word2: str) -> bool:
            list1 = list(word1)
            list2 = list(word2)

            dict1 = dict()
            dict2 = dict()

            for i in list1:
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1
            for i in list2:
                if i in dict2:
                    dict2[i] += 1
                else:
                    dict2[i] = 1
            return dict1 == dict2

        if not strs:
            return [[""]]

        result = list()
        length = len(strs)
        valid = [1] * length
        for i in range(length):
            templist = []
            if valid[i] == 1:
                templist.append(strs[i])
                valid[i] = 0
            # else:
            #     pass
            for j in range(i+1, length):
                if helper(strs[i], strs[j]) is True and valid[j] == 1:
                    templist.append(strs[j])
                    valid[j] = 0
            if templist:
                result.append(templist)
        return result


s = Solution1()
a = s.groupAnagrams(["a"])



class Solution:  # overtime
    def groupAnagrams(self, strs):
        temp_dict = {}
        for i in strs:
            # Hash_result = self.HashMapFunc1(i)
            Hash_result = self.HashMapFunc2(i)
            if Hash_result in temp_dict:
                temp_dict[Hash_result].append(i)
            else:
                temp_dict[Hash_result] = [i]
        return temp_dict.values()

    def HashMapFunc1(self, temp_src):
        return ''.join(sorted(list(temp_src)))

    def HashMapFunc2(self, temp_src):
        key = [0] * 26
        for i in temp_src:
            key[ord(i) - ord('a')] += 1

        return ''.join(str(i) for i in key)


s = Solution()
print(s.groupAnagrams(["bdddddddddd", "bbbbbbbbbbc"]))

