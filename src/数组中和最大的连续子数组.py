def largest_sum_in_list(inputs):
    if not inputs:
        return 0

    # 在i个数字中连续子数组和最大的值
    max_tmp = inputs[0]

    max_sum = inputs[0]

    for i in range(1, len(inputs)):

        max_tmp = max(inputs[i], max_tmp + inputs[i])

        if max_tmp > max_sum:
            max_sum = max_tmp

    return max_sum


if __name__ == "__main__":

    print(largest_sum_in_list([2, -3, 6, 2, 1, -5, -5, 8]))
