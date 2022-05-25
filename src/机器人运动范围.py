def movie_count(threshold,row,col):
    "机器人运动范围"

    # 解题思路：dfs + 递归

    if row <= 0 or col <= 0 or threshold < 0:
        return 0

    move_matrix = [[False for j in range(col)] for i in range(row)]

    count = dfs(move_matrix,row,col,0,0,threshold)
    return count

def dfs(move_matrix,row,col,i,j,threshold):
    # 如果达到数组的边界或者当前的坐标已经被访问过或者行坐标和列坐标的数位之和大于threshold, 说明不能再继续移动,则跳出
    if i < 0 or j < 0 or i >= row or j >= col or move_matrix[i][j] or not cal_threshold(i,j,threshold):
        return 0

    move_matrix[i][j] = True

    return 1 + dfs(move_matrix,row,col,i+1,j,threshold) + dfs(move_matrix,row,col,i-1,j,threshold)+dfs(move_matrix,row,col,i,j+1,threshold)+dfs(move_matrix,row,col,i,j-1,threshold)



def cal_threshold(i,j,threshold):
    x = i // 10 +  i % 10
    y = j // 10 +  j % 10
    if sum([x,y]) > threshold:
        return False
    else:
        return True