# 解题思路
    # 双指针

def func(array):
    pos = 0
    neg = 0

    # 用来标记当前是找正数还是负数
    flag = True

    n = len(array)

    for i  in range(n):
        # 找正数
        if flag:
            pos = i
            
            while pos < n and  array[pos] <= 0:
                pos += 1
            
            if pos >= n:
                break
            
            # 取出找到的正数
            tmp_value = array[pos]
            # i~pos之间的数整体向右平移一位
            while pos > i:
                array[pos] = array[pos-1]
                pos -= 1

            # 将正数填充到起始的位置
            array[i] = tmp_value
            
            # 开始找负数
            flag = not flag 

        # 找负数
        else:
            neg = i
            
            while neg < n and array[neg] > 0:
                neg += 1
            
            if neg >= n:
                break
            
            # 取出找到的正数
            tmp_value = array[neg]
            # i~pos之间的数整体向右平移一位
            while neg > i:
                array[neg] = array[neg-1]
                neg -= 1

            # 将正数填充到起始的位置
            array[i] = tmp_value
            
            # 开始找正数
            flag = not flag 

    return array



print(func([-1,2,3,4,-1,-5,-6]))