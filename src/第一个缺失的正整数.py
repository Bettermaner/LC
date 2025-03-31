# 解题思路
    # 先找出所有值小于等于该数组长度的数字，并将其按照数字的大小当做索引，插入到数组对应的位置中
    # 然后再遍历一遍数组，将第一次出现 （当前数字的值和当前数组的索引不相等时），返回当前索引+ 1 大小即可。


import copy
def run(inputs):
    
    arr = copy.deepcopy(inputs)
    
    for index,value in enumerate(inputs):
        corr = value -1
        if corr != index and value >0 and value <= len(inputs):
            tmp = arr[corr] 
            arr[corr] = value
            arr[index] = tmp
    print(arr)
    
    for index,value in enumerate(arr):
        if index != value -1:
            return index + 1
            
    return index + 1
                
    
    
print(run([1,0,4,2,5,-1]))