# 数组可能是 先升后降、中间有平台段（重复值）、多个连续相等的峰值；

# 输入: [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]
# 输出: 5 （位置3~5之间都有可能）

# 输入: [1, 3, 2]
# 输出: 3 或者 None（如果题目要求严格大于）

# 输入: [5, 5, 5]
# 输出: 所有都是“平台型”峰值

# 方法一：线性扫描（O(n)）
# 最简单的方法是遍历整个数组，找到任意一个满足条件的峰值：

def findPeakElement(nums):
    n = len(nums)
    for i in range(n):
        left = nums[i - 1] if i > 0 else float('-inf')
        right = nums[i + 1] if i < n - 1 else float('-inf')
        if nums[i] >= left and nums[i] >= right:
            return i
    return -1


# 方法二：改进的二分查找（O(log n)）
# 虽然存在重复值，但我们可以对标准二分法进行一些修改，使其在遇到重复值时也能继续搜索。

# 思路：
# 如果 nums[mid] < nums[mid + 1] → 峰值一定在右边
# 如果 nums[mid] > nums[mid + 1] → 峰值一定在左边或 mid 自己
# 如果 nums[mid] == nums[mid + 1] → 需要特殊处理（比如向两边都尝试找）


def findPeakElement(nums):
    n = len(nums)
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            # 峰值在右侧
            left = mid + 1
        elif nums[mid] > nums[mid + 1]:
            # 峰值在左侧或当前mid就是峰值
            right = mid
        else:
            # 相等的情况：nums[mid] == nums[mid + 1]
            # 尝试向右移动
            left = mid + 1

    # 检查是否确实是峰值
    def is_peak(i):
        left_val = nums[i - 1] if i > 0 else float('-inf')
        right_val = nums[i + 1] if i < n - 1 else float('-inf')
        return nums[i] >= left_val and nums[i] >= right_val

    if is_peak(left):
        return left
    return -1

print(findPeakElement([1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1]))  # 输出: 4 或 5（索引）
print(findPeakElement([5, 5, 5]))                         # 输出: 1（任意一个）
