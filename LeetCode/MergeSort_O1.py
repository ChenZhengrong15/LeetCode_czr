# coding: UTF-8
# 旨在实现一个 O(1) 的merge sort方法


class Solution:
    # def mergeSort_O1(self, arr: List[int], left: int, right: int) -> List[int]:
    def merge(self, arr, l, r, m, v):
        i = l
        j = m + 1
        k = l
        # 归并
        while i <= m and j <= r:
            if arr[i] % v <= arr[j] % v:
                arr[k] = arr[k] + (arr[i] % v) * v
                k += 1
                i += 1
            else:
                arr[k] = arr[k] + (arr[j] % v) * v
                k += 1
                j += 1
        # 归并剩余元素
        while i <= m:
            arr[k] = arr[k] + (arr[i] % v) * v
            k += 1
            i += 1
        while j <= r:
            arr[k] = arr[k] + (arr[j] % v) * v
            k += 1
            j += 1
        # 获取原序列值
        for n in range(l, r+1):
            arr[n] = arr[n] // v
        # print(arr)

    def merge_sort_rec(self, arr, left, right, maxval):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort_rec(arr, left, mid, maxval)
            self.merge_sort_rec(arr, mid+1, right, maxval)
            self.merge(arr, left, right, mid, maxval)

    def mergeSort_O1(self, arr):
        maxval = max(arr) + 1
        length = len(arr)
        self.merge_sort_rec(arr, 0, length-1, maxval)
        return arr


if __name__ == '__main__':
    s = Solution()
    a = [1, 4, 2, 6, 8, 2, 7]
    print(s.mergeSort_O1(a))

