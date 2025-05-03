
# 🧠 解题思路：DFS + 回溯
# 我们可以从每个格子出发，尝试进行深度优先搜索（DFS），寻找目标单词。

# 步骤说明：
# 遍历整个网格中的每一个字符；
# 如果当前字符和目标单词的第一个字符相同，就从这里开始 DFS；
# 在 DFS 中：
# 如果当前位置字符不匹配 → 返回 False
# 否则标记该位置为已访问（比如把字符改为 # 或者用 visited 数组）
# 朝四个方向继续搜索（上、下、左、右）
# 找到完整单词路径后返回 True
# 搜索完成后要恢复现场（回溯）


# ⏱️ 时间与空间复杂度分析
# 时间复杂度: 最坏情况下每个格子都要做一次 DFS，每次最多走 len(word) 步。
# 总时间复杂度大约是 O(m × n × 4^L)，其中 L 是 word 的长度。
# 空间复杂度: 主要是递归栈的空间，最深为 L，所以是 O(L)

def find_string_in_matrix(matrix,string):
    "二维矩阵中查找存在的字符串"

    # 解题思路: dfs + 递归
    # 矩阵 shape : [m,n]
    if not matrix:
        return False

    m = len(matrix)
    n = len(matrix[0]) 

    # 对每个字符依次递归,每个字符都可以上下左右移动
    # 可以把字符上下左右的字符看做是一个4叉树,每个节点都对应4个子节点
    for i in range(m):

        for j in range(n):

            if dfs(matrix,string,i ,j,0):
                return True
    else:
        return False

def dfs(matrix,string,i,j,index):

    if (i > len(matrix)-1 or j > len(matrix[0])-1 or i < 0 or j < 0 or matrix[i][j] != string[index] ):
        return False

    # 如果字符长度已经达到,说明已经完全匹配上
    if index == len(string) -1:
        return True
    
    tmp = matrix[i][j]
    ## 修改当前坐标的值,防止指针走回来
    matrix[i][j] = "*"
    ## 走递归，沿着当前坐标的上下左右4个方向查找
    res = dfs(matrix,string,i+1,j,index+1) or dfs(matrix,string,i-1,j,index+1) or dfs(matrix,string,i,j+1,index+1) or dfs(matrix,string,i,j-1,index+1)
    
    ## 递归之后再把当前的坐标复原
    matrix[i][j] = tmp
    
    return res


print(find_string_in_matrix([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))