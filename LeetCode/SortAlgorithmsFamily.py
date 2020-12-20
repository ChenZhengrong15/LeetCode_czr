# coding: utf-8
# 实现各种排序算法


class SortFamily:
    def __init__(self):
        pass

    @staticmethod
    def bubble_sort(sequence):
        """
        比较相邻的元素，如果第一个比第二个大，就交换他们；
        对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
        针对所有的元素重复以上步骤，除了最后一个；
        重复步骤 1~3，直到排序完成。
        """
        n = len(sequence)
        for i in range(n):
            for j in range(0, n-1):
                if sequence[j] > sequence[j+1]:
                    sequence[j+1], sequence[j] = sequence[j], sequence[j+1]
        return sequence

    @staticmethod
    def select_sort(sequence):
        """
        首先在未排序序列中找到最小(大)元素，存放到排序序列的起始位置；
        再从剩余未排序元素中继续寻找最小(大)元素，然后放到已排序序列的末尾；
        重复第二步，直到所有元素均排序完毕。
        """
        n = len(sequence)
        for i in range(n-1):
            min_idx = i
            for j in range(i+1, n):
                if sequence[j] < sequence[i]:
                    min_idx = j
            sequence[min_idx], sequence[i] = sequence[i], sequence[min_idx]
        return sequence

    @staticmethod
    def insert_sort(sequence):
        """
        从第一个元素开始，该元素可以认为已经被排序；
        取出下一个元素，在已经排序的元素序列中从后向前扫描；
        如果该元素(已排序)大于新元素，将该元素移到下一位置；
        重复步骤 3，直到找到已排序的元素小于或者等于新元素的位置；
        将新元素插入到该位置后；
        """
        n = len(sequence)
        for i in range(1, n):
            while i > 0 and sequence[i-1] > sequence[i]:
                sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
                i = i - 1
        return sequence

    @staticmethod
    def shell_sort(sequence):
        """
         希尔排序基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
         按增量序列的个数 k，对序列进行 k 趟排序；
         每趟排序，根据对应的增量 ti,将待排序序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
        """
        n = len(sequence)
        d = n
        while n > 0:
            d //= 2
            if d > 0:
                for i in range(d, n):
                    for j in range(i - d, n - d, d):
                        if sequence[j] > sequence[j + d]:
                            sequence[j], sequence[j + d] = sequence[j + d], sequence[j]
            else:
                break
        return sequence

    @staticmethod
    def merge_sort(sequence):
        def merge(left, right):
            result = []
            while left and right:
                if left[0] < right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            while left:
                result.append(left.pop(0))
            while right:
                result.append(right.pop(0))
            return result

        n = len(sequence)
        if n < 2:
            return sequence
        mid = n // 2
        l, r = sequence[: mid], sequence[mid + 1:]
        return merge(l, r)

    @staticmethod
    def quick_sort(sequence):
        def recursive(begin, end):
            if begin > end:
                return
            l, r = begin, end
            pivot = sequence[l]
            while l < r:
                while sequence[r] > pivot:
                    r -= 1
                while sequence[l] <= pivot:
                    l += 1
                sequence[l], sequence[r] = sequence[r], sequence[l]
            sequence[l], sequence[begin] = pivot, sequence[l]  # 原数组在 l=r 处的值
            recursive(begin, l-1)
            recursive(r+1, end)
        recursive(0, len(sequence)-1)
        return sequence

    def heap_sort(self, sequence):
        pass

    def counting_sort(self, sequence):
        pass

    def bucket_sort(self, sequence):
        pass
