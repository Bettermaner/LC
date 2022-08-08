# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

def func(nums):
    tmp_jump = 0
    n = len(nums)
    for i in range(n):
        if i <= tmp_jump:
            tmp_jump = max(nums[i] + i,tmp_jump)
        if tmp_jump >= n-1:
            return True
    else:
        return False
    