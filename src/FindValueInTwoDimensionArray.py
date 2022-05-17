def find_value_in_two_dimension(array,target):
    "在二维数组中寻找指定的数是否存在"

    if not array:
        return False
        
    # 二维数组的长和宽
    m = len(array)
    n = len(array[0])

    i = 0
    j = n -1

    #记录i,j两个指针
    #从第一行最后一列开始与target做比较
    while i <= m -1 and j >= 0:

        # 当target大于当前的值说明target大于当前行的左侧所有的值
        # i指针向下移动一行
        if target > array[i][j]:
            i += 1

        # 当target小于当前的值说明target可能会于当前行的左侧里面的值相等
        # j指针向左移动一个列
        elif target < array[i][j]:
            j -= 1

        # 如果相等则找到了,直接返回
        else:
            return True
    else:
        return False


