# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

def func(array):

    res = []
    t_array = []


    def dfs(array,t_array,res):

        if len(t_array) != 0 and t_array not in res:
            res.append(t_array)

        if len(array) == 0:
            return 

        # 当前字符不加入
        dfs(array[1:],t_array,res)
        # 当前字符加入
        t = t_array + array[:1]
        dfs(array[1:],t,res)

    dfs(array,t_array,res)

    return [[]]+ res 

print(func([1,2,3]))