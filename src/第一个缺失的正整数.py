# 解题思路
    # 先找出所有值小于等于该数组长度的数字，并将其按照数字的大小当做索引，插入到数组对应的位置中
    # 然后再遍历一遍数组，将第一次出现 （当前数字的值和当前数组的索引不相等时），返回当前索引+ 1 大小即可。


def func(array):

    for index,value in enumerate(array):
        correct = value - 1
        if correct != index and value > 0 and value <= len(array):
            tmp = array[correct]
            array[correct] = value
            array[index] = tmp
        

    for index,value in array:
        correct = value -1
        if correct != index:
            return index + 1

    return index + 1