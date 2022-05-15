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
