# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
# 其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]

# 解题思路
    # 单调栈，维护一个单调递减的栈，保存温度在数组中对应的索引位置

def func(temperatures):
    n = len(temperatures)
    res = [0] * n

    stack = []

    for index,t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            pre_index = stack.pop()
            day = index - pre_index
            res[pre_index] = day

        stack.append(index)

    return res

print(func([73,74,75,71,69,72,76,73]))