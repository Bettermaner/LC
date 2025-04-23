# 解题思路
    # 动态规划
    # 当前对应的数，能接雨水的值是等于 min(当前数左边的柱子最大高度，当前数右边的柱子最大高度) - 当前数对应的柱子高度
    # 我们可以提前将数组中每个数对应的 （左边的柱子最大高度、右边的柱子最大高度）算出来，存储好
    # 然后直接遍历数组，取对应的值，计算总的接雨水量

def func(array):
    n = len(array)
    if n < 3:
        return 0

    result = 0

    # 从左边的数开始算
    left_max_h = [array[0]]
    # 反过来的从右边的数开始算
    right_max_h = [array[-1]]

    for i in range(1,n):
        left_max_h.append(max(array[i],left_max_h[-1]))
        right_max_h.append(max(array[n-1-i],right_max_h[-1]))

    for index ,value in enumerate(array):
        left_max = left_max_h[index]
        right_max = right_max_h[n-1-index]
        result += max(0,min(left_max,right_max) - value)

    return result