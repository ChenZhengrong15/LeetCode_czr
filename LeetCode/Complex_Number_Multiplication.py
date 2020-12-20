# coding:UTF-8
# 计算复数的乘法


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        idx1 = a.index('+')
        idx2 = b.index('+')
        num11 = int(a[0: idx1])
        num12 = int(a[idx1+1: -1])
        num21 = int(b[0: idx2])
        num22 = int(b[idx2+1: -1])
        real = str(num11 * num21 - num12 * num22)
        unreal = str(num11 * num22 + num12 * num21)
        return real + '+' + unreal + 'i'


s = Solution()
print(s.complexNumberMultiply('1+-1i', '1+-1i'))


