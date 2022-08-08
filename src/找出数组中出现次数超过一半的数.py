# 1.数组总长度为n，找出出现 次数大于 n/2 的数
# 解题思路
    # 摩尔投票法
    # 从第一个数开始，先令count=1，遇到相同的就加1，遇到不同的就减1，减到0就重新换下个数开始计数，到最后是哪个数，那么那个数就是众数。

def func(nums):
    major = nums[0]
    vote = 1
    n = len(nums)

    for i in range(1,n):
        if vote == 0:
            major = nums[i]
            vote = 1

        elif nums[i] == major:
            vote += 1

        else:
            vote -= 1

    return major



# 2.数组总长度为n，找出出现 次数大于 n/3 的数
# 分析
    # 个数大于 n/2，最多只能有一个数满足条件
    # 个数大于 n/3，最多只能有两个数满足条件

def func(nums):
    n = len(nums)
    if not n:
        return nums

    major1 = 0
    major2 = 0
    vote1 = 0
    vote2 = 0

    for i in range(n):
        if major1 == nums[i]:
            vote1 += 1
        elif major2 == nums[i]:
            vote2 += 1

        elif vote1 == 0:
            major1 = nums[i]
            vote1 = 1

        elif vote2 == 0:
            major2 = nums[i]
            vote2 = 1

        else:
            vote1 -= 1
            vote2 -= 1

    count1 = 0
    count2 = 0
    for num in nums:
        if num == major1:
            count1 += 1
        elif num == major2:
            count2 += 1

    res = []
    if count1 > n //3:
        res.append(major1)

    if count2 > n// 3:
        res.append(major2)

    return res