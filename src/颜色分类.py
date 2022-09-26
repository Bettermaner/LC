# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 必须在不使用库的sort函数的情况下解决这个问题。

# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]

# 解题思路
    # 单指针

def func(array):
    index = 0

    n = len(array)

    # 先找0
    for i in range(n):
        if array[i] == 0:
            array[i],array[index] = array[index],array[i]
            index += 1

    # 再找1
    for  j in range(index,n):
        if array[j] == 1:
            array[j],array[index] = array[index],array[j]
            index += 1

    return array

print(func([2,0,2,1,1,0]))