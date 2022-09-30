# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10

    # 解题思路
    # 单调栈（单调递增的栈），找出当前柱子对应的左侧、右侧，第一个比该柱子小的柱子
    # 需要从左到右、从右到左遍历数组，得到每根柱子对应的左右边界。
    # 然后 当前柱子高度 * （right - left -1 ）得到当前柱子i下最大的矩形面积

    # 具体操作
    # 栈中存放了 j 值。从栈底到栈顶，j 的值严格单调递增，同时对应的高度值也严格单调递增；
    # 当我们枚举到第 i 根柱子时，我们从栈顶不断地移除，栈顶元素满足 height[stack[-1]] >= height[i]的情况，
    # 在移除完毕后，栈顶的 j 值就一定满足 height[stack[-1]] < height[i]
    # 此时 j 就是 i 左侧且最近的小于其高度的柱子。

    # 这里会有一种特殊情况。如果我们移除了栈中所有的 j值，那就说明 ii 左侧所有柱子的高度都大于height[i]
    # 那么我们可以认为 i 左侧且最近的小于其高度的柱子在位置 j= -1,或 n，
    # 它是一根「虚拟」的、高度无限低的柱子。这样的定义不会对我们的答案产生任何的影响，
    # 我们也称这根「虚拟」的柱子为「哨兵」。

def func(height):

    n = len(height)
    if n == 0:
        return 0

    left_b = [0] * n
    right_b = [0] * n

    # 先从左到右找柱子的左侧边界
    stack = []
    for i in range(n):
        while stack and height[stack[-1]] >= height[i]:
            stack.pop()
            
        if not stack:
            # 哨兵
            j = -1
        else:
            j = stack[-1]

        left_b[i] = j
        stack.append(i)

    
    # 先从右往左找柱子的右侧边界
    stack = []
    for i in range(n-1,-1,-1):
        while stack and height[stack[-1]] >= height[i]:
            stack.pop()
        
        if not stack:
            # 哨兵
            j = n
        else:
            j = stack[-1]

        right_b[i] = j
        stack.append(i)

    return max([ (right_b[i] - left_b[i] -1) * height[i] for i in range(n)])

print(func([2,1,5,6,2,3]))