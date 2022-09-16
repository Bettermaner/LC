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