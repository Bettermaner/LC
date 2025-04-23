# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]

# 解题思路
    # 二分法

    # 由于数组已经排序，因此整个数组是单调递增的，我们可以利用二分法来加速查找的过程。

    # 考虑 \textit{target}target 开始和结束位置，其实我们要找的就是数组中「第一个等于 \textit{target}target 的位置」（记为 \textit{leftIdx}leftIdx）和「第一个大于 \textit{target}target 的位置减一」（记为 \textit{rightIdx}rightIdx）。

    # 二分查找中，寻找 \textit{leftIdx}leftIdx 即为在数组中寻找第一个大于等于 \textit{target}target 的下标，寻找 \textit{rightIdx}rightIdx 即为在数组中寻找第一个大于 \textit{target}target 的下标，然后将下标减一。两者的判断条件不同，为了代码的复用，我们定义 binarySearch(nums, target, lower) 表示在 \textit{nums}nums 数组中二分查找 \textit{target}target 的位置，如果 \textit{lower}lower 为 \rm truetrue，则查找第一个大于等于 \textit{target}target 的下标，否则查找第一个大于 \textit{target}target 的下标。


from turtle import right


def func(array,target):

    # 是否是需要大于等于target
    flag = True

    left_index = find_index(array,target,flag)
    right_index = find_index(array,target,not flag) - 1

    if right_index < len(array) and left_index <= right_index and array[left_index] == target and array[right_index]:
        return (left_index,right_index)

    return (-1,-1)

def find_index(array,target,flag):

    n = len(array)
    left = 0
    right = n -1
    res = 0
    while left < right:
        mid = (left + right)
        if array[mid] > target or (flag and array[mid] >= target):
            right = mid - 1
            res = mid
        else:
            left = mid + 1

    return res


print(func([5,7,7,8,8,10],8))


# 方法2
def binary_search_first(arr, target):
    """
    查找目标元素在数组中的第一个位置
    """
    left, right = 0, len(arr) - 1
    first_pos = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first_pos = mid
            right = mid - 1  # 继续向左查找
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_pos

def binary_search_last(arr, target):
    """
    查找目标元素在数组中的最后一个位置
    """
    left, right = 0, len(arr) - 1
    last_pos = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            last_pos = mid
            left = mid + 1  # 继续向右查找
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last_pos

def find_first_and_last(arr, target):
    """
    在排序数组中查找目标元素的第一个位置和最后一个位置
    """
    first_pos = binary_search_first(arr, target)
    last_pos = binary_search_last(arr, target)
    return first_pos, last_pos

# 示例
arr = [1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
target = 2
first_pos, last_pos = find_first_and_last(arr, target)
print(f"目标元素 {target} 的第一个位置是：{first_pos}")
print(f"目标元素 {target} 的最后一个位置是：{last_pos}")