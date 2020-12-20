# 频次大于数组长度的一半
# 摩尔投票


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1

        count = 0
        major = None

        for i in range(len(nums)):
            if count == 0:
                major = nums[i]
                count += 1
            else:
                if nums[i] == major:
                    count += 1
                else:
                    count -= 1
        if count > 0:
            count_1 = 0
            for i in nums:
                if i == major:
                    count_1 += 1
            if count_1 > len(nums)/2:  # 是每次篇判断一次慢，还是全部求出之后再判断慢呢？
                return major
            return -1
        else:
            return -1

