# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
# 其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]

# 解题思路
    # 单调栈，维护一个单调递减的栈，保存温度在数组中对应的索引位置

# 对于每一天的温度t，检查栈是否为空以及当前温度t是否大于栈顶元素对应的温度。如果是，则说明找到了一个比栈顶元素温度高的日子。
# 通过弹出栈顶元素并计算当前索引与栈顶元素索引之间的差值，我们可以得知需要等待多少天才能遇到更高温度的日子。
def func(temperatures):
    n = len(temperatures)
    res = [0] * n

    stack = []

    for index,t in enumerate(temperatures):
        # 当栈不为空且当前温度t大于栈顶所对应的温度时，进行处理，循环找在过去比当前温度低的日期对应的索引
        while stack and t > temperatures[stack[-1]]:
            pre_index = stack.pop() # # 弹出栈顶元素（即找到一个比当前温度低的旧温度的索引）
            day = index - pre_index
            res[pre_index] = day

        stack.append(index) # 将当前温度的索引压入栈中

    return res

print(func([73,74,75,71,69,72,76,73]))