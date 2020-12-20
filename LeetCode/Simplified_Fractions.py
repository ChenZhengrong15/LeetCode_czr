class Solution:
    def simplifiedFractions(self, n: int):
        def common_divisor(l, m):
            while True:
                k = l % m
                l = m
                m = k
                if k == 0:
                    return l
        result = []
        for i in range(2, n+1):
            for j in range(1, i):
                d = common_divisor(j, i)
                if d == 1:
                    temp_str = str(j) + "/" + str(i)
                    result.append(temp_str)
        return result


s = Solution()
print(s.simplifiedFractions(5))
