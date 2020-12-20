# coding:UTF-8
# 实现堆结构
# 堆 (heap) 是一种经过排序的完全二叉树，其中任一非叶子节点的值均不大于（或不小于）其左孩子和右孩子节点的值。
# 又被为优先队列(priority queue)。尽管名为优先队列，但堆并不是队列。
# 堆一般采用完全二叉树
# 堆中的每一个节点都大于其左右子节点（大顶堆）， 或者堆中每一个节点都小于其左右子节点（小顶堆）


class Heap:
    def __init__(self):
        self.data_list = []

    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        # 以大顶堆为例
        # 先把元素放在最后，向前堆化
        # 不断与父节点比较，比父节点大则交换，直到最后
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)

        while parent is not None and self.data_list[parent] < self.data_list[index]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def remove_max(self):
        # 将最末尾元素设置为堆顶，再不断的向后堆化
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]

        del self.data_list[-1]
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        # 堆化函数
        # 从 index 开始，自上向下堆化（大顶堆）
        max_index = len(self.data_list) - 1
        while True:
            max_value_index = index
            child_index = 2 * index
            if child_index + 1 <= max_index and self.data_list[child_index + 1] > self.data_list[max_value_index]:
                max_value_index = child_index + 1
            if child_index + 2 <= max_index and self.data_list[child_index + 2] > self.data_list[max_value_index]:
                max_value_index = child_index + 2
            if max_value_index == index:
                break
            self.swap(max_value_index, index)
            index = max_value_index


if __name__ == '__main__':
    myheap = Heap()
    for i in range(10):
        myheap.insert(i+1)
    print("堆：", myheap.data_list)
    print("删除堆顶元素：", [myheap.remove_max() for _ in range(len(myheap.data_list))])



