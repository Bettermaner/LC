# 给一个数组，求一个k值，使得前k个数的方差 + 后面n-k个数的方差最小
# https://cloud.tencent.com/developer/article/1108835
def run(inputs):
    
    # 从左往右计算累计方差和
    left = cal_var(inputs)
    # 从右往左计算累计方差和，然后再将结果倒过来，形成left[i-1] + right[i] 表示以i为分割点的，两部分数据的方差和
    right = cal_var(inputs[::-1])[::-1]
    
    min_var = float("inf")
    min_var_index = 0
    for i in range(1,len(inputs)):
        if left[i-1] + right[i] < min_var:
            min_var = left[i-1] + right[i]
            min_var_index = i -1 
    print(left)
    print(right)
    return min_var,min_var_index
    
    
        
def cal_var(inputs):
    
    sum_square = 0
    sum_val = 0
    
    sum_var_array = []
    
    for i in range(len(inputs)):
        val = inputs[i]
        sum_square += val**2
        sum_val += val
        # 方差 =  所有数平方和的均值 - 所有数和的均值的平方
        sum_var = (sum_square/(i+1)) - (sum_val/(i+1)) ** 2 
        sum_var_array.append(sum_var)
    
    return sum_var_array
        
                
    
    
print(run([1,0,4,2,5,1]))