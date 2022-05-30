def print_numbers(n):
    "输入数字 n,按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3,则打印出 1、2、3 一直到最大的 3 位数 999"
    numbers = 10 ** n
    res = []
    
    for num in range(1,numbers):
        res.append(num)    
    return res