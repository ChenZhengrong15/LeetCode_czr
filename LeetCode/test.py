def quick_select(sequence):
    def recursive(begin,end):
        #
        if begin>end:
            return
        #左右分别取开始索引与结束索引
        left,right=begin,end
        #基准取数列首个元素
        pivot=sequence[left]
        #当左的索引值小于右索引值
        while left<right:
            #右索引所表示的值大于基准值，索引-1，向前移动
            while left<right and sequence[right]>pivot:
                right=right-1
            #左索引所表示的值大于基准值，索引+1，向后移动
            while left<right and sequence[left]<=pivot:
                left=left+1
            #交换找到的两个不符合判断条件值
            # print(left, right, pivot)
            sequence[left],sequence[right]=sequence[right],sequence[left]
            # print(sequence)
        #将基准值填充进去，并重新赋值开始索引
        sequence[left],sequence[begin]=pivot,sequence[right]
        #左右两侧递归使用快速排序
        recursive(begin,left-1)
        recursive(right+1,end)
    recursive(0,len(sequence)-1)
    return sequence

if __name__ == '__main__':
    sequence = [12, 27, 46, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    print(sequence)
    print(quick_select(sequence))
