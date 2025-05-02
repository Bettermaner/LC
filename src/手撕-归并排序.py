# 时间复杂度：归并排序的时间复杂度是 O(n log n)，其中 n 是数组的长度。这是因为每次都将数组分成两半（这需要 O(log n) 的递归深度），
# 并且在每个层次上都要遍历所有元素（O(n)）来进行合并操作。
# 空间复杂度：由于归并排序需要额外的空间来存储临时数组（用于合并操作），其空间复杂度是 O(n)。
# 虽然可以优化到 O(1) 空间复杂度（称为原地归并排序），但这通常会牺牲时间效率，并且实现起来更为复杂。

def merge_sort(inputs):
    """归并排序"""
    if len(inputs) <= 1:
        return inputs

    # 将列表分成更小的两个列表
    mid = int(len(inputs) / 2)

    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = merge_sort(inputs[:mid])
    right = merge_sort(inputs[mid:])

     # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left,right)



def merge(left,right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []

    left_index = 0
    right_index = 0

    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1

        elif left[left_index] > right[right_index]:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]

    return result


if __name__ == "__main__":
    inputs = [16,1,2,3,1,5,4,7,8,9,22,3,54,13,11,20,12,4,5,6,25]
    print(merge_sort(inputs))