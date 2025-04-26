# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# 深度优先搜索

# DFS函数：
# 首先检查当前子集t_array是否非空且不在结果集中。如果是，则将其加入结果集res。
# 如果输入数组array为空，说明已经到达了叶子节点，返回。
#  对于每个元素，有两种选择：
    ##  不包含当前元素：递归调用dfs，参数为剩余部分array[1:]和当前子集t_array。
    ## 包含当前元素：创建一个新的列表t，它是t_array加上当前元素array[:1]，然后递归调用dfs，参数为剩余部分array[1:]和新子集t。

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