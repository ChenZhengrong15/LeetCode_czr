# coding: UTF-8
# 搜索一个有序的二维矩阵
# 充分利用有序矩阵的特性才可以获得最好的复杂度，从左下角开始查找


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        low, high = matrix[0][0], matrix[m-1][n-1]
        if target < low or target > high:
            return False

        row, col = m - 1, 0
        while col < n and row >= 0:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False
