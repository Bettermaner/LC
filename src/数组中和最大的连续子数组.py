def largest_sum_in_list(inputs):
    if not inputs:
        return 0

    # 在i个数字中连续子数组和最大的值
    max_tmp = inputs[0]

    max_sum = inputs[0]

    for i in range(1, len(inputs)):

        max_tmp = max(inputs[i], max_tmp + inputs[i]) # 这一步实际上是在决定是否将当前元素加入到现有的子数组中（如果加入后的和更大，就加入）还是从当前元素重新开始一个新的子数组（从当前这个元素，重新开始统计）。

        if max_tmp > max_sum:
            max_sum = max_tmp

    return max_sum


if __name__ == "__main__":

    print(largest_sum_in_list([2, -3, 6, 2, 1, -5, -5, 8]))

# 若还需要考虑返回最大和对应的子数组，应该怎么做？

def maxSumSubarray(nums):
    if not nums:
        return 0, []  # 如果输入数组为空，返回0和空列表

    # 初始化最大和、当前和以及结果为第一个元素
    max_sum = current_sum = nums[0]  # 最大和初始化为第一个元素
    start = end = temp_start = 0  # 起始位置、结束位置和临时起始位置初始化为0

    for i in range(1, len(nums)):  # 从第二个元素开始遍历数组
        num = nums[i]  # 当前数字

        # 如果当前和加上当前数字小于当前数字，则重新开始计算子数组
        if current_sum + num < num:
            current_sum = num  # 当前和更新为当前数字
            temp_start = i  # 更新临时起始位置为当前位置
        else:
            current_sum += num  # 否则，当前和加上当前数字

        # 更新最大和及对应的起始和结束位置
        if current_sum > max_sum:
            max_sum = current_sum  # 更新最大和为当前和
            start = temp_start  # 更新起始位置为临时起始位置
            end = i  # 更新结束位置为当前位置

    return max_sum, nums[start:end + 1]  # 返回最大和及其对应的子数组

# 示例用法
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 示例数组
max_value, subarray = maxSumSubarray(nums)  # 调用函数获取最大和及其子数组
print("最大和:", max_value)  # 输出: 最大和: 6
print("对应子数组:", subarray)  # 输出: 对应子数组: [4, -1, 2, 1]

