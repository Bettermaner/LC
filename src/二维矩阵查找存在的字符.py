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