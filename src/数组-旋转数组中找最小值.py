def find_min_rotated_array(inputs):
    "旋转数组中找出最小值"

    # 解题思路: 二分法

    if not inputs:
        return None

    left = 0
    right = len(inputs) -1

    while left < right:

        mid = int((left + right) / 2)

        # 如果中指针大于右指针,说明最小值在右边部分
        if inputs[mid] > inputs[right]:
            left = mid + 1
         # 如果中指针小于右指针,说明最小值在左边部分
        elif inputs[mid] < inputs[right]:
            right = mid
        # 如果中指针等于右指针,右指针向左一下
        else:
            right -= 1

    return inputs[right]

# 2.旋转数组的中位数
# 如果求旋转数组的中位数
    # 先确定最小值的位置，然后根据中位数的距离最小值的长度，从最小值位置移动，即求中位数感觉应该可行.