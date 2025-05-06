# 解题思路
    # 二分法

def func(array,target):

    if not array:
        return -1
    
    left = 0
    right = len(array) - 1

    
    while left  < right:
        mid = (left + right) // 2
        if array[left] > array[mid]:
            if array[left] < target or array[mid] > target:
                right = mid
            else:
                left = mid + 1
        elif array[left] < array[mid]:
            if array[left] <= target <= array[mid]:
                right = mid
            else:
                left = mid + 1
        else:
            if array[mid] == target:
                right = left
            else:
                left = left + 1

    return left if array[left] == target else -1