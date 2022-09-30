# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9

# 解题思路
    # 哈希表

def func(array):

    res = 0
    n = len(array)
    m = {}

    for i in range(n):
        m[array[i]] = 1

    for i in range(n):
        v = array[i]

        # 找出每组连续序列中的第一个数
        if v-1 not in m:
            cur_v = v
            cur_res = 1

        while cur_v + 1 in m:
            cur_v += 1
            cur_res += 1

        res = max(cur_res,res)

    return res

print(func([0,3,7,2,5,8,4,6,0,1]))