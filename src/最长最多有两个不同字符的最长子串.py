# 解题思路
    # 滑动窗口 + 哈希表
    # 哈希表记录每个数在窗口出现的频次
    # 维护一个左指针一个右指针，
    # 从左边开始右滑动，当发现当前的数频次大于1则滑动左指针，并将滑到当前的数据从哈希表中减一,直至不重复就停止左指针滑动。
    # 维护一个不重复子数组最大长度max_length

def max_length(string,k):
    max_length = 0

    left = 0
    right = 0

    map = {}

    while right  < len(string):
        right_value = string[right]

        if right_value not in map:
            map[right_value] = 1
        else:
            map[right_value] = map[right_value] + 1

        while map[right_value] > k:
            left_value = string[left]
            map[left_value] = map[left_value] -1
            left += 1

        max_length = max(max_length,right - left + 1)
        right += 1
        
    return max_length


print(max_length("addssa",2))