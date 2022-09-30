# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 说明：

# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# 解题思路
    # 异或位运算

def singleNumber(nums) -> int:
    n = len(nums)
    x = nums[0]
    for i in range(1,n):
        y = nums[i]
        x = x ^ y 

    return x

print(singleNumber([2,2,1,3,3,4,5,5,4]))