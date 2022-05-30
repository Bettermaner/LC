def power(base,e):
    "数值的整数次方"

    # 如果e是负数,则将base取倒数,e取-e转化为正数
    if e < 0:
        base = 1/ base
        e = -e 
    res = 1
    
    for i in range(e):
        res *= base
    return res