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



# 通义大模型版本

# 时间与空间复杂度分析
# 时间复杂度: O(n)，每个元素最多入队和出队一次。
# 空间复杂度: O(k)，队列中最多存储 k 个索引。

# 移除不在窗口范围内的元素：通过 while queue and queue[0] < i - k + 1:
# 判断队首元素是否已经不在当前窗口范围内，如果是，则需要将其移除。这里用 queue = queue[1:] 来模拟 popleft()。
# 保持队列递减：在将新元素加入队列之前，先检查队尾元素是否小于当前元素，如果是，则移除队尾元素，直到找到一个不小于当前元素的位置或队列为空。
# 这样可以保证队列中的索引对应的数组值是严格递减的。
# 记录结果：当窗口形成后（即 i >= k - 1），每次都将队首元素对应的值加入结果列表中，因为队首元素始终是当前窗口的最大值。

def maxSlidingWindow(nums, k):
    if not nums or k <= 0:
        return []

    result = []
    queue = []  # 普通列表模拟双端队列

    for i in range(len(nums)):
        # 移除不在窗口范围内的元素（队首）
        while queue and queue[0] < i - k + 1:
            queue = queue[1:]  # 手动模拟 popleft()

        # 移除所有比当前元素小的元素（从队尾）
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()  # 使用 pop() 来移除队尾元素

        queue.append(i)

        # 窗口形成后才记录最大值
        if i >= k - 1:
            result.append(nums[queue[0]])

    return result