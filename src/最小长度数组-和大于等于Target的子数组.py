# 给定一个含有 n 个正整数的数组和一个正整数 target 。

# 找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

# 示例 1：

# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。


# 🧠 解题思路：滑动窗口法（双指针）
# 步骤说明：
# 使用两个指针 left 和 right 表示窗口的左右边界；
# 初始时窗口为空，逐步向右移动 right 指针，将元素加入当前总和 current_sum；
# 当 current_sum ≥ target 时，尝试向右移动 left 指针，缩小窗口大小，同时更新最小长度；
# 如果找不到满足条件的子数组，返回 0。
# ⚠️ 这个方法的时间复杂度为 O(n)，因为每个元素最多被访问两次（一次进窗口，一次出窗口）


# ⏱️ 时间 & 空间复杂度分析
# 时间复杂度: O(n)，其中 n 是数组长度
# 空间复杂度: O(1)，只用了几个变量


def minSubArrayLen(target: int, nums) -> int:
    n = len(nums)
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(n):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0