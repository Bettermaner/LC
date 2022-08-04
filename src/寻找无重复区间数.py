# 解题思路
    # 贪心算法
    # 简单说是，每一步做出一个局部最优选择，最终结果是全局最优。

def func(intervals):
    intervals = sorted(intervals,key=lambda x:(x[1],x[0]))
    length = len(intervals)
    if length == 0:
        return 0

    res = 0
    end = intervals[0][1]

    for inter in intervals:
        if inter[0] >= end:
            res += 1
            end = inter[1]

    return res