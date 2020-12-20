# # coding: UTF-8
# 二分法查找


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        low = matrix[0][0]
        high = matrix[n-1][m-1]

        while low < high:
            count = 0
            mid = (low + high) // 2
            for i in range(n):
                j = n - 1
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1  # 这是篇python自己下标的影响，统计比 mid 小的元素个数
            if count >= k:  # 调节所在
                high = mid
            else:
                low = mid + 1
        return low

