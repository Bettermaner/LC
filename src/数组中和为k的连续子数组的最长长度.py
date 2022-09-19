# 解题思路
    # 双指针
    # 方法1
    # 维护一个sum，初始值=0
    # right指针向右滑动，每滑一次，sum加下当前滑到的值，并且判断是否 >= k
    # 如果没有满足，则继续向右滑
    # 如果满足则将sum 减去当前left指针指向的值并将left向右滑动一个次
    # 直到right指针到达尾部

    # 方法2
    # 提前计算好 每一个索引下，左边的所有数的和
    # sum[left:right] = sum(right) - sum(left -1) 

def func(lst,k):

    t = []
    for i in  range(len(lst)):
        t.append(sum(lst[:i+1]))


    left = 0
    sum_v = 0

    res = 0
    for i in range(len(lst)):
        sum_v += lst[i]

        while sum_v >= k and left <= i:
            if sum_v == k:
                res = max(res,i - left + 1)
            sum_v -= lst[left]
            left += 1
        

    return res


print(func([4,4,5,2,1,2],5))


# 若是求数组中和为k的连续子数组的最短长度
def func(lst,k):

    t = []
    for i in  range(len(lst)):
        t.append(sum(lst[:i+1]))


    left = 0
    sum_v = 0

    # 最坏的情况是lst里所有的值相加才能等于k，所以这里设置为 len(lst) + 1
    res = len(lst) + 1

    for i in range(len(lst)):
        sum_v += lst[i]

        while sum_v >= k and left <= i:
            if sum_v == k:
                res = min(res,i - left + 1)
            sum_v -= lst[left]
            left += 1
        

    return res


print(func([4,4,5,2,1,2],5))