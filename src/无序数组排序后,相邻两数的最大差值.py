# 解题思路
    # 分桶法
    # 根据最大值与最小值确定边界
    # 然后按照(max - min ) / n+1的距离，分成n+1个桶
    # 将数据依次按照桶边界放入其中，并记录每个桶内最大值与最小值
    # 比较所有相邻两个非空桶，左桶内的最大值与右桶内的最小值的差值，找出最大差值即可

def func(array):
    n = len(array)
    max_value = array[0]
    min_value = array[0]

    result = 0

    for i in range(1,n):
        max_value = max(max_value,array[i])
    
    
    for i in range(1,n):
        min_value = min(min_value,array[i])

    
    d = (max_value - min_value) / n+1

    bucket = {}
    left = min_value
    for i in range(n+1):
        left = left + i * d
        right = left + (i+ 1) * d
        bucket[i] = [left,right] 

    buckets = [[] for i in range(n+1)]
    for index ,value in enumerate(array):
        for key in bucket:
            minv ,maxv = bucket[key]
            if value >= minv and value <= maxv:
                buckets[key].append(value)
        

    m_buckets = [[] for i in range(n+1)]

    for index ,value in enumerate(buckets):
        if value:
            min_v = value[0]
            max_v = value[0]
            for v in value:
                min_v = min(min_v,v)
                max_v = max(max_v,v)
            m_buckets[index] = [min_v,max_v]

    i = 0
    m_buckets = [value for value in m_buckets if value]
    while i < len(m_buckets)-1 :
        _,left_max= m_buckets[i]
        right_min,_ = m_buckets[i+1]
        diff = right_min - left_max
        result = max(result,diff)
        i += 1

    return result
            