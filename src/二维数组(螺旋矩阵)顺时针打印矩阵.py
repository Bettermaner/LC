

def print_matrix(matrix):
    "输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字"
    # 解题思路： 边界模拟法
    # 设置 上下左右4个边界
    # 当遍历到右边界，上边界则+1，当遍历到下边界，右边界则-1
    # 当遍历到左边界，下边界则-1，当遍历到上边界，左边界则+1
    # 停止条件，当上边界 > 下边界 and 左边界 > 右边界
    result = []
    if not len(matrix):
        return result
    up = 0
    down = len(matrix) - 1

    left = 0
    right = len(matrix[0]) - 1

    while left <= right and up <= down:

        for i in range(left, right + 1):
            result.append(matrix[up][i])
        up += 1
        if up > down:
            break

        for i in range(up, down+1):
            result.append(matrix[i][right])
        right -= 1

        if right < left:
            break

        i = right
        while i >= left:
            result.append(matrix[down][i])
            i -= 1
        down -= 1

        if down < up:
            break

        i = down
        while i >= up:
            result.append(matrix[i][left])
            i -= 1
        left += 1

        if left > right:
            break
    return result
