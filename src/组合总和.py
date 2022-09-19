# 你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
# 找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。


# 编码通过 深度优先遍历 实现，使用一个列表，在 深度优先遍历 变化的过程中，
# 遍历所有可能的列表并判断当前列表是否符合题目的要求，成为「回溯算法」

# 以 target = 7 为 根结点 ，创建一个分支的时 做减法 ；
# 每一个箭头表示：从父亲结点的数值减去边上的数值，得到孩子结点的数值。边的值就是题目中给出的 candidate 数组的每个元素的值；
# 减到 00 或者负数的时候停止，即：结点 00 和负数结点成为叶子结点；
# 所有从根结点到结点 00 的路径（只能从上往下，没有回路）就是题目要找的一个结果。

def func(array,target):

    result = []
    path  = []

    def dfs(array,index,target,path,result):

        if target == 0:
            result.append(path)
            return 
        if target < 0 :
            return

        for i in range(index,len(array)):
            dfs(array,i,target-array[i],path+[array[i]],result)


    dfs(array,0,target,path,result)

    return result


print(func([2,3,6,7],7))