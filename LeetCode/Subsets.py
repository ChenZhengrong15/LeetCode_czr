# coding:UTF-8
# 求全部子集
# 递归， 遍历一遍，主次将未采用的元素加入到之前已存在的集合中


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for i in nums:
            result += [curr + [i] for curr in result]

        return result

