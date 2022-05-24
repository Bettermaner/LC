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