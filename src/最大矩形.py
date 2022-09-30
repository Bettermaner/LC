# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6

# 解题思路
    # 单调栈，与柱状图中的最大矩形类似，只不过会根据row，计算多个柱状图的最大矩形面积


def maximalRectangle(matrix) -> int:
    res_nums = [0]*len(matrix[0])
    max_s = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if int(matrix[i][j]) == 0:
                # 如果当前row上的对应的col值为0，则该col对应的柱子高度为0，因为断开了
                res_nums[j] = 0
            res_nums[j] += int(matrix[i][j])
        max_s = max(max_s, get_max_s(res_nums) )   # 求出当前形成柱形的面积，与之前比较取最大的面积
    return max_s



def get_max_s(height):

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


print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))