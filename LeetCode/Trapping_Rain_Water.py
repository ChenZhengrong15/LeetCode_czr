# coding:UTF-8
# 接雨水问题


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        #
        length = len(height)
        maxleft, maxright, result = [0] * length, [0] * length, 0
        # 初始化
        maxleft[0], maxright[length-1] = height[0], height[length-1]
        # 边界条件
        for i in range(1, length):
            maxleft[i] = max(height[i], maxleft[i-1])

        for j in range(length-2, -1, -1):
            maxright[j] = max(height[j], maxright[j+1])

        for k in range(1, length - 1):
            if min(maxleft[k], maxright[k]) > height[k]:
                result += min(maxleft[k], maxright[k]) - height[k]
        return result



class Solution1:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        left, right = 0, n-1
        result = 0
        maxleft = height[0]
        maxright = height[n-1]
        while left <= right:
            maxleft = max(height[left], maxleft)
            maxright = max(height[right], maxright)
            if maxleft < maxright:
                result += maxleft - height[left]
                left += 1
            else:
                result += maxright - height[right]
                right -= 1
        return result



class Solution2:
    def trap(self, height: List[int]) -> int:
        pass
    


