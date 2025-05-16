# 解题思路
    # 贪心算法
    # 简单说是，每一步做出一个局部最优选择，最终结果是全局最优。

# 找出无重复区间数
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


# 找出需要移除区间的最小数量
# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。
# 注意 只在一点上接触的区间是 不重叠的。例如 [1, 2] 和 [2, 3] 是不重叠的。

def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
    
        # 按照每个区间的结束时间进行排序
        intervals.sort(key=lambda x: x[1])
        
        # 初始化计数器和上一个区间的结束时间
        count = 0  # 需要移除的区间数
        prev_end = intervals[0][1]  # 上一个区间的结束时间
        n = len(intervals)
        
        # 从第二个区间开始遍历
        for i in range(1, n):
            start, end = intervals[i]
            
            # 如果当前区间的开始时间 >= 上一个区间的结束时间，说明没有重叠
            if start >= prev_end:
                # 更新上一个区间的结束时间为当前区间的结束时间
                prev_end = end
            else:
                # 否则，这个区间需要被移除
                count += 1
        
        return count