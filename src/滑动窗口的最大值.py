def max_in_winodw(array,size):
    "给定一个长度为 n 的数组 nums 和滑动窗口的大小 size ，找出所有滑动窗口里数值的最大值。"
    res = []
    if not array or size > len(array):
        return res

    # 记录窗口左边界与右边界索引
    # 记录当前窗口中最大值对应的索引
    # 记录当前窗口中的最大值
    window_left,window_right = 0, size -1
    max_value = array[0]
    max_index = -1

    while window_right < len(array):

        # 如果此时最大值对应的索引在窗口里面
        if max_index >= window_left and max_index <= window_right:
            # 将最大值与窗口内最右边的值做比较，因为最右边的值是这次新加入到窗口的值
            # 如果最右边的值大于最大值，则替换成当前的最大值
            if max_value < array[window_right]:
                max_value = array[window_right]
                max_index = window_right
        # 如果此时最大值对应的索引在窗口里面
        else:
            # 说明最大值已经被滑出窗口，需要在窗口中找出当前的最大值
            tmp = window_left
            max_index = window_left
            max_value = array[window_left]
            while tmp <= window_right:
                if max_value < array[tmp]:
                    max_value = array[tmp]
                    max_index = tmp
                tmp += 1

        window_left += 1
        window_right += 1

        res.append(max_value)
        
    return res
