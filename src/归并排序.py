

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