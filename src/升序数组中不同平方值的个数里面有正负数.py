# 解题思路
    # 要求时间复杂度o(n),空间复杂度o(1)
    # 双指针，还需要一个pre指针，记录前一个时刻的值
    # 每次遍历都需要与pre值比较下，如果不相等就+1

def func(array):
    left = 0
    right = len(array) -1

    pre = -1
    res = 0

    while left < right:
        if (abs(array[left]) > abs(array[right])):
                if abs(array[left]) != pre:
                    res += 1
                    pre = abs(array[left])
                left += 1
        else:
            if abs(array[right]) != pre:
                res += 1 
                pre = abs(array[right])
            right -= 1

    return res


print(func([-9,-3,-1,1,1,1,3,9,9]))