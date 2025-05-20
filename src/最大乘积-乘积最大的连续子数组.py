def largest_product_in_list(inputs):
    "乘积最大的连续子数组"
    if not inputs:
        return 0
    # 在i个数字中连续子数组乘积最大的值
    max_tmp = inputs[0]
    # 在i个数字中连续子数组乘积最小的值
    min_tmp = inputs[0]

    max_product = inputs[0]

    for i in range(1, len(inputs)):
        # 防止max_tmp在计算完max后被min引用，所以用mx,mn表示此次循环中的max_tmp与min_tmp
        mx, mn = max_tmp, min_tmp

        max_tmp = max(mx * inputs[i], mn * inputs[i], inputs[i])
        min_tmp = min(mx * inputs[i], mn * inputs[i], inputs[i])

        max_product = max(max_tmp, max_product)

    return max_product


if __name__ == "__main__":

    print(largest_product_in_list([2, -3, 2, -5, -5]))

# 若还需要考虑返回最大乘积对应的子数组，应该怎么做？

def maxProductSubarray(nums):
    if not nums:
        return 0, []  # 如果输入数组为空，返回0和空列表

    # 初始化最大值、最小值和结果为第一个元素
    max_product = min_product = result = nums[0]  # 最大值、最小值和结果初始化为第一个元素
    start_max = end_max = start_min = end_min = 0  # 起始位置和结束位置初始化为0
    result_start = result_end = 0  # 结果的起始位置和结束位置初始化为0

    for i in range(1, len(nums)):
        num = nums[i]  # 当前数字

        # 如果当前数字是负数，交换最大值和最小值的位置
        if num < 0:
            max_product, min_product = min_product, max_product  # 交换最大值和最小值
            start_max, start_min = start_min, start_max  # 交换最大值和最小值的起始位置

        # 计算当前的最大值和最小值
        if num > max_product * num:
            max_product = num  # 如果当前数字大于当前最大值乘以当前数字，则更新最大值为当前数字
            start_max = i  # 更新最大值的起始位置为当前位置
        else:
            max_product *= num  # 否则，最大值乘以当前数字

        if num < min_product * num:
            min_product = num  # 如果当前数字小于当前最小值乘以当前数字，则更新最小值为当前数字
            start_min = i  # 更新最小值的起始位置为当前位置
        else:
            min_product *= num  # 否则，最小值乘以当前数字

        # 更新结果
        if max_product > result:
            result = max_product  # 更新结果为当前最大值
            result_start = start_max  # 更新结果的起始位置为最大值的起始位置
            result_end = i  # 更新结果的结束位置为当前位置

    return result, nums[result_start:result_end + 1]  # 返回最大值及其对应的子数组



print(maxProductSubarray([2, 3, -2, 4]))  # 输出应该是 (6, [2, 3])
print(maxProductSubarray([-2, 0, -1]))    # 输出应该是 (0, [0])
print(maxProductSubarray([-2, -3, -4]))   # 输出应该是 (12, [-3, -4])
print(maxProductSubarray([0, 2]))         # 输出应该是 (2, [2])
nums = [2, 3, -2, 4,5]
# nums = [2, 3,-4,-5, 0, 11, 10]
# nums = [ -3, 0, -11]
max_value, subarray = maxProductSubarray(nums)
print("最大乘积:", max_value)  # 输出: 最大乘积: 6
print("对应子数组:", subarray)  # 输出: 对应子数组: [2, 3]