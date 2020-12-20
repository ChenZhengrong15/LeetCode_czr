# coding: UTF-8
# 三维形体的表面积


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    result += grid[i][j] * 4 + 2
                if i > 0:
                    result -= 2 * min(grid[i-1][j], grid[i][j])
                if j > 0:
                    result -= 2 * min(grid[i][j-1], grid[i][j])
        return result
