# coding： UTF-8
# 第k个排列， 1 <= n <= 9; 1 <= k <= n!


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1  # (k-1) // m + 1 即为 k/m 向上取整的结果，python 只有向下取整的运算，没有向上取整的运算
        ans = list()
        valid = [1] * (n+1)

        for i in range(1, n+1):
            order = k // factorial[n-i] + 1  # a_i
            # 将 a_i 加入到 ans 中
            for j in range(1, n+1):
                order -= valid[j]  # 只能选取没有被选取过的数字
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            # k 需要变化
            k = k % factorial[n - i]

        return ''.join(ans)
