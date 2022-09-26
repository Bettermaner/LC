# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。


# 解题思路
    # 翻转代替旋转
    # 先水平翻转 ，再对角线翻转


def func(array):
    m = len(array)

    # 水平翻转
    for i in range(m//2):
        for j in range(m):
            array[i][j],array[m-1-i][j] = array[m-1-i][j],array[i][j]

    # 对角线翻转
    for i in range(m):
        for j in range(i):
            array[i][j],array[j][i] = array[j][i],array[i][j]

    return array

print(func([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))