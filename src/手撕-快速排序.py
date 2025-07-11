# 解题思路
    # 1. 从待排序列表中选取一个基准数据(通常选取第一个数据)。

    # 2. 将待排序列表中所有比基准数据小的元素都放到基准数据左边，所有比基准数据大的元素都放到基准数据右边(升序排列，降序反之)。
    # 用基准数据进行分割操作后，基准数据的位置就是它最终排序完成的位置，第一轮排序完成。

    # 3. 递归地对左右两个部分的数据进行快速排序。即在每个子列表中，选取基准，分割数据。直到被分割的数据只有一个或零个时，列表排序完成

# 平均时间复杂度：O(n log n)，其中 n 是数组长度。
# 原地排序版本：由于不需要额外的存储空间来存放分割后的子数组，因此空间复杂度为 O(log n)，主要是由递归调用栈引起的。

def quick_sort(array,start,end):

    if start >= end:
        return 

    mid = array[start]
    left = start
    right = end

    while left < right:

        while array[right] >= mid and left < right:
            right -= 1
        # 如果右边的小与当前值，则和left交换
        array[left] = array[right]

        while array[left] < mid and left < right:
            left += 1
        # 如果左边的大于当前值，则和right交换
        array[right] = array[left]

    array[left] = mid

    quick_sort(array,start,left-1)
    quick_sort(array,left + 1,end)


array = [2,3,2,1,5,6,4,7,8,2]
quick_sort(array,0,len(array)-1)
print(array)