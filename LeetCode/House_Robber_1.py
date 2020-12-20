class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        length = len(nums)

        if length == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, length):
            first, second = second, max(first+nums[i], second)

        return second
