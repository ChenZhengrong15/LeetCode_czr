# coding:UTF-8
# 煎饼排序


class Solution:
    def pancakeSort(self, arr):
        if arr == sorted(arr):
            return []

        def inverse_k_elements(array, k):
            if k > len(array):
                return None
            array_1 = array[0: k]
            array_1 = array_1[::-1]
            array_1.extend(array[k:])
            return array_1

        result = []
        l = len(arr)
        # arr_1 = []
        # while not len(arr_1) == l:
        while True:
            max_element = max(arr)
            # arr_1.append(max_element)
            idx = arr.index(max_element)
            result.append(idx+1)
            arr = inverse_k_elements(arr, idx+1)
            length = len(arr)
            result.append(length)
            arr = inverse_k_elements(arr, length)
            arr = arr[0: length-1]
            if arr == sorted(arr):
                break

        return result


if __name__ == '__main__':
    s = Solution()
    a = [3, 2, 4, 1]
    print(s.pancakeSort(a))

