# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

# 请不要使用除法，且在 O(n) 时间复杂度内完成此题


def func(array):

    k = 1

    n = len(array)
    
    res = [0 for i in range(n)]
    for i in range(n):
        res[i] = k # 此时数组表示当前索引左边所有数的乘积，当i=0时，默认左边所有数乘积=1
        k = k * array[i]

    k = 1
    for j in range(n-1,-1,-1):
        res[j] = res[j] * k
        k = k * array[j]

    return res

print(func([-1,1,0,-3,3]))