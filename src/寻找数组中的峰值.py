# 峰值元素是指其值大于左右相邻值的元素。

# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。

# 解题思路：
    # 二分法

# 找到mid下标
# 如果array[mid] > array[mid+1] 说明 当前mid在右峰下坡中
    # 峰值在左侧，令right = mid
# 如果array[mid] < array[mid+1] 说明 当前mid在左峰上坡中
    # 峰值在右侧 ，令left = mid + 1


def func(array):
    left =0
    right = len(array) - 1

    while left < right:
        mid = (left + right) // 2

        if array[mid] > array[mid+1]:
            right = mid
        elif array[mid] < array[mid+1]:
            left = mid + 1
        else:
            left += 1

    return left

print(func([1,2,1,3]))
