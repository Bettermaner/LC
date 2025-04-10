# 解题思路
    # 归并排序
    # 核心代码是分解后，合并的那部分
    # 当右边数组中的数，小于左边数组中的数时，则左边数组[left:]的数均能组成逆序对。

# 两个数组找逆序对
pair = 0
# 合并
def merge_and_sort(left,right):
    left_index = 0
    right_index = 0
    tmp = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            left_index += 1
            tmp.append(left[left_index])
        else:
            right_index += 1
            tmp.append(right_index)
            pair += len(left[left_index:])

    tmp = tmp + left[left_index:]
    tmp = tmp + right[right_index:]

    return tmp
    
# 一个数组找逆序对
def merge_and_sort(left, right):
    left_index = 0
    right_index = 0
    tmp = []
    inv_count = 0  # 记录逆序对的数量

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            tmp.append(left[left_index])
            left_index += 1
        else:
            tmp.append(right[right_index])
            right_index += 1
            # 当右边的一个元素小于左边的某个元素时，
            # 表示存在逆序对，逆序对的数量等于左侧剩余未处理元素的数量
            inv_count += len(left) - left_index

    # 将剩余的元素添加到结果列表中
    tmp.extend(left[left_index:])
    tmp.extend(right[right_index:])

    return tmp, inv_count  # 返回排序后的数组和逆序对的数量


def merge_sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    # 递归地分割数组
    left_sorted, left_inv = merge_sort_and_count(arr[:mid])
    right_sorted, right_inv = merge_sort_and_count(arr[mid:])
    
    # 合并两个有序数组并计算逆序对
    merged_arr, split_inv = merge_and_sort(left_sorted, right_sorted)
    
    # 总的逆序对数量是三个部分的总和：左半部分、右半部分以及跨越两部分的逆序对
    total_inv = left_inv + right_inv + split_inv
    
    return merged_arr, total_inv


# 示例调用
arr = [7, 5, 6, 4]
sorted_arr, inversions = merge_sort_and_count(arr)
print("Sorted array:", sorted_arr)
print("Number of inversions:", inversions)

