class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        l, r = matrix[0][0], matrix[m-1][n-1]
        while l < r:
            count = 0
            mid = (r+l)//2
            for i in range(n):
                j = n-1
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count = count+j+1
            if count >= k:
                r = mid
            else:
                l = mid+1
        return l
