# 解题思路
    # 归并排序
    # 核心代码是分解后，合并的那部分
    # 当右边数组中的数，小于左边数组中的数时，则左边数组[left:]的数均能组成逆序对。
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
    
