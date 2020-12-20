# 翻转图像
# 对称位置相等的需要变为 1-原值


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for r in A:
            for i in range((len(r)+1) // 2):
                if r[i] == r[-1-i]:
                    r[i] = r[-1-i] = 1 - r[i]
        return A

