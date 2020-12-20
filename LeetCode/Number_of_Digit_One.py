# coding: UTF-8
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# 题解：https://leetcode-cn.com/problems/number-of-digit-one/solution/gelthin-zhu-ge-shu-wei-ji-suan-by-gelthin/


class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        k = 1
        while k <= n:
            count += (n // (k * 10)) * k + min(max((n % (10*k) - k + 1), 0), k)  # 分段函数
            k *= 10
        return count


s = Solution()
a = s.countDigitOne(18)
print(a)
