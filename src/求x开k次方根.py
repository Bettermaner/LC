# 1.带浮点的值开k次方根，要求返回的值不仅仅包含整数，也带浮点
# 二分法
def func(x,k):

    left = 0
    right = x

    while (right - left) > 0.1 ** 3:
        mid = (left + right) / 2

        if mid ** k  > x:
            right = mid
        elif mid ** k < x:
            left = mid
        else:
            left = mid

    return left
        

print(func(100,3))


def func(x,k,n):
    left = 0

    if x > 1:
        right = x
    else:
        right = 1

    while (right - left) > 0.1 ** n:
        mid = (left + right) / 2

        if mid ** k  > x:
            right = mid
        elif mid ** k < x:
            left = mid
        else:
            left = mid

    return round(left,n)
        

print(func(0.04,3))