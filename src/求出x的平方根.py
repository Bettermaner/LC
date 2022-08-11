def my_sqrt(x):
    if x == 0:
        return 0

    i = 0
    while not (i * i < x and (i + 1) * (i + 1) > x):
        i += 1
        if i * i == x:
            break

    return i 


# 1.带浮点的值开平方根，要求返回的值不仅仅包含整数，也带浮点
# 二分法
def func(x,n):

    left = 0
    right = x

    while (right - left) > 0.1 ** n:
        mid = (left + right) // 2

        if mid ** 2  > x:
            right = mid
        elif mid ** 2 < x:
            left = mid
        else:
            left = mid

    return left
        