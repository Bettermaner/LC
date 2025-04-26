array = [2,4,5,6,8,1]
res = [4,5,6,8,-1,-1]

array = [2,1,5,3,5,1]
res = [5,5,-1,5,-1,-1]


# 解题思路
    # 单调栈
    # 维护一个单调递减的栈，当遍历到的数 大于栈顶的元素的值，则栈顶元素出栈，并将遍历的数据加入栈顶
    # 直至这个遍历到的数 小于栈顶的元素的值

    # 那当前出栈的元素对应的左边第一个大的数据就是当前遍历到的这个数

def func(array):

    stack = []

    n = len(array)

    res = [0 for i in range(n)]

    for i in range(n):
        
        while stack and array[stack[-1]] < array[i]:
            index = stack.pop()
            res[index] = array[i]

        stack.append(i)

    if stack:
        for index in stack:
            res[index] = -1

    return res

print(func([2,4,5,6,8,1]))

        
print(func([2,1,5,3,5,1]))