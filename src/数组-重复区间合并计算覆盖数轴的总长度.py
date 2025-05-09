
# 总结
# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)



def merge_intervals(intervals):
    """
    合并重叠或相邻的区间，并计算覆盖数轴的总长度
    
    参数:
    intervals -- 一个列表，包含形如[start, end]的区间
    
    返回:
    一个元组，包含合并后的区间列表和覆盖的总长度
    """
    # 处理空列表情况
    if not intervals:
        return [], 0
    
    # 按区间的开始值进行排序
    intervals.sort(key=lambda x: x[0])
    
    # 初始化合并后的区间列表
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # 如果当前区间与上一个区间重叠或相邻
        if current[0] <= last[1]:
            # 合并两个区间
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            # 添加新的区间
            merged.append(current)
    
    # 计算覆盖的总长度
    total_length = sum(end - start for start, end in merged)
    
    return merged, total_length

# 示例用法
if __name__ == "__main__":
    # 示例区间列表
    intervals = [
        [1, 3],
        [2, 5],
        [7, 10],
        [9, 12],
        [15, 18]
    ]
    
    merged, total_length = merge_intervals(intervals)
    
    print("合并后的区间:", merged)
    print("覆盖的总长度:", total_length)