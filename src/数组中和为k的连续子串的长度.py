# 解题思路
    # 双指针
    # 提前计算好 每一个索引下，左边的所有数的和
    # sum[left:right] = sum(right) - sum(left -1) 

def func(lst,k):

    t = []
    for i in  range(len(lst)):
        t.append(sum(lst[:i+1]))


    left = 0
    sum_v = 0

    res = 0
    for i in range(len(lst)):
        sum_v += lst[i]

        while sum_v >= k and left <= i:
            if sum_v == k:
                res = max(res,i - left + 1)
            sum_v -= lst[left]
            left += 1
        

    return res


print(func([4,4,5,2,1,2],5))