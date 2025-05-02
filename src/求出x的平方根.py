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



# 通义大模型版本

# 只保留整数部分的情况
# 时间复杂度	O(log x)
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


# 二分查找法
def sqrt_binary_search(x: float, epsilon=1e-3) -> float:
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    if x == 0:
        return 0
    
    left = 0.0
    right = max(1.0, x)
    
    while right - left > epsilon:
        mid = (left + right) / 2.0
        square = mid * mid
        
        if abs(square - x) < epsilon:
            return mid
        elif square < x:
            left = mid
        else:
            right = mid
            
    # 返回左右端点中更接近实际平方根的那个
    return (right + left) / 2.0

print(sqrt_binary_search(0.2))


# 牛顿迭代法
# 原理
# 牛顿迭代法是一种用于寻找函数零点的数值分析方法。对于求解 sqrt(x)，我们可以将其转化为求解方程 f(y) = y^2 - x = 0 的正根。
# 迭代公式：
# 给定初始估计值 y0，迭代公式为：
# 对于 f(y)=y^2−x，其导数为 =2y。根据牛顿迭代法的一般公式yn+1=yn − （f(yn)/f′(yn)）
#  带入上述公式中：𝑦𝑛+1=𝑦𝑛−(𝑦𝑛^2 - x)/2y = (yn + x/yn) /2

# 所以得到 yn+1 = (yn + x/yn) /2 ,这里是根据泰勒公式展开得到的，

# 当相邻两次迭代的结果差值小于某个很小的阈值时，认为已经找到了足够接近真实平方根的近似值。

# O(log(1/ε))，其中 ε 是所需精度。


def sqrt_newton(x: float, epsilon=1e-5) -> float:
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    if x == 0:
        return 0
    
    # 初始猜测值
    guess = x / 2.0
    
    while True:
        new_guess = (guess + x / guess) / 2.0
        
        # 检查是否达到精度要求
        if abs(new_guess - guess) < epsilon:
            return new_guess
        
        guess = new_guess

print(sqrt_newton(4.6))
