# coding: UTF-8
# 求一个整数序列中的最大子序列之和


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1<=len(nums)<=2*10**4
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        for i in range(1, length):
            dp[i] = max(dp[i - 1]+nums[i], nums[i])
        return max(dp)


class Solution2:
    def maxSubArray(self, nums: List[int])-> int:
        length = len(nums)
        result = nums[0]
        pre = 0
        for i in range(length):
            pre = max(pre + nums[i], nums[i])
            result = max(result, pre)
        return result
