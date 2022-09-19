# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 返回容器可以储存的最大水量。

# 解题思路：
    # 双指针
    # S(面积) = (height[j] - height[i]) * (j-i)

    # 在每个状态下，无论长板或短板向中间收窄一格，都会导致水槽 底边宽度 -1−1​ 变短：

    # 若向内 移动短板 ，水槽的短板 min(h[i], h[j])min(h[i],h[j]) 可能变大，因此下个水槽的面积 可能增大 。
    # 若向内 移动长板 ，水槽的短板 min(h[i], h[j])min(h[i],h[j])​ 不变或变小，因此下个水槽的面积 一定变小 。
    # 因此，初始化双指针分列水槽左右两端，循环每轮将短板向内移动一格，并更新面积最大值，直到两指针相遇时跳出；即可获得最大面积。

def func(height):

    left = 0
    right = len(height) - 1

    res = 0
    while left < right:
        if height[left] < height[right]:
            res = max(res,(right - left) * height[left])
            left += 1
        else:
            res = max(res,(right - left) * height[right])
            right -= 1

    return res 

print(func([1,8,6,2,5,4,8,3,7]))