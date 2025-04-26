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

    if x > 1:
        right = x
    else:
        right = 1

    while (right - left) > 0.1 ** n:
        mid = (left + right) / 2

        if mid ** 2  > x:
            right = mid
        elif mid ** 2 < x:
            left = mid
        else:
            left = mid

    return round(left,n)
        

print(func(0.04,3))



# 只保留整数部分的情况
def mySqrt(x: int) -> int:
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    if x == 0 or x == 1:
        return int(x)

    left, right = 0, max(1, x)  # 对于x<1的情况，right设为1；否则设为x

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
            
    # 返回最接近但不大于实际平方根的整数值
    return right

print(my_sqrt(0.02))