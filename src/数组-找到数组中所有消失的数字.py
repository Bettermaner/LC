# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
# 请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

# 输入：nums = [4,3,2,7,8,2,3,1]
# 输出：[5,6]

# 解题思路
# 原地修改数组。

# 这个思想来自于长度为 N 的数组可以用来统计 1~N1  各数字出现的次数；
# 题目给出的数组的长度正好为 N，所以可以原地修改数组实现计数。

# 当前元素是 nums[i]，那么我们把第 nums[i] −1 位置的元素 乘以 -1，表示这个该位置出现过。
# 当然如果 第 nums[i] −1 位置的元素已经是负数了，表示 nums[i] 已经出现过了，就不用再把第 nums[i] - 1 位置的元素乘以 -1。
# 最后，对数组中的每个位置遍历一遍，如果 i 位置的数字是正数，说明 i 未出现过。

def func(array):

    n = len(array)
    res = []
    for i  in range(n):
        v = array[i]
        if array[abs(v)-1] > 0:
            array[abs(v)-1] = array[abs(v)-1] * -1

    for j in range(n):
        if array[j] > 0:
            res.append( j+ 1)

    return res


print(func([4,3,2,7,8,2,3,1]))


# 返回数组中消失的一个数字
def func2(nums):
    n = len(nums)
    # 计算从0到n的总和
    total_sum = n * (n + 1) // 2  # 使用整除以确保结果为整数
    # 计算数组中所有数字的总和
    array_sum = sum(nums)
    
    # 缺失的数字就是两者的差值
    return total_sum - array_sum