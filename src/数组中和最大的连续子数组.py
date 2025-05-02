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