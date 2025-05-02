# 给定一个整数数组 nums，代表一个排列（数字可能包含重复元素），请原地修改数组，使其变为 字典序上“下一个更大”的排列。
# 如果不存在更大的排列，则返回最小的排列（即升序排列）。

# 输入: nums = [1,2,3]
# 输出: [1,3,2]

# 输入: nums = [3,2,1]
# 输出: [1,2,3]

# 输入: nums = [1,1,5]
# 输出: [1,5,1]



# 解题思路：这个算法是基于字典序生成算法的经典步骤，总共分为四步：

# 从后向前查找第一个相邻升序对 (i, i+1)，使得 nums[i] < nums[i+1]。
# 此时 nums[i+1:] 是降序的。
# 在 nums[i+1:] 中从后向前找第一个大于 nums[i] 的元素 nums[j]。
# 交换 nums[i] 和 nums[j]。
# 反转 nums[i+1:]，使其变为升序（因为之前是降序，所以反转即可）。
# 这样就能得到下一个更大的排列。

# 时间复杂度分析
# 时间复杂度：O(n)
# 每一步最多遍历整个数组一次。
# 空间复杂度：O(1)
# 原地操作，没有使用额外空间。

def nextPermutation(nums):
    n = len(nums)
    
    # 步骤1：从右往左找第一个比右边小的数
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    if i >= 0:
        # 步骤2：从右往左找第一个比 nums[i] 大的数
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # 步骤3：交换这两个数
        nums[i], nums[j] = nums[j], nums[i]
    
    # 步骤4：翻转 i+1 到末尾的部分
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# 示例测试
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # 输出: [1, 3, 2]