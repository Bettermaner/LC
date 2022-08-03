# 解题思路
    # dfs递归

# 1. 岛屿数量

def count_lands(lands):

    m = len(lands)
    n = len(lands[0])

    count = 0
    for i in range(m):
        for j in range(n):

            if lands[i][j] == "1":
                dfs(lands,i,j)
                count += 1
    
    return count

def dfs(lands,i,j):
    m = len(lands)
    n = len(lands[0])

    if (i == 0 or j ==0 or i >= m or j >= n or lands[i][j] == "0"):
        return 
    # 访问过的地方标记为0，说明已经访问过
    lands[i][j] = "0"
    # 以该点的上下左右方向进行递归
    dfs(lands,i,j-1)
    dfs(lands,i,j+1)
    dfs(lands,i+1,j)
    dfs(lands,i-1,j)


# 2.岛屿的最大面积
def max_area_lands(lands):

    m = len(lands)
    n = len(lands[0])

    max_area = 0
    for i in range(m):
        for j in range(n):
            count = 0
            if lands[i][j] == "1":
                area = dfs(lands,i,j,count)
                max_area =  max(area,max_area)
    
    return max_area

def dfs(lands,i,j,count):
    m = len(lands)
    n = len(lands[0])

    if (i == 0 or j ==0 or i >= m or j >= n or lands[i][j] == "0"):
        return 0
    count += 1

    lands[i][j] = "0"

    dfs(lands,i,j-1,count)
    dfs(lands,i,j+1,count)
    dfs(lands,i+1,j,count)
    dfs(lands,i-1,j,count)

    return count


# 3.岛屿的周长
# 观察后发现，从陆地走到水域或者从陆地走向边界时，都会出现一条边，既为周长的一部分，依次统计即可
# 需要注意的是，当标记访问过的陆地时不能再使用0，会和水域混淆调，因此用2标记

def long_lands(lands):

    m = len(lands)
    n = len(lands[0])

    long = 0
    for i in range(m):
        for j in range(n):
            if lands[i][j] == "1":
                count = dfs(lands,i,j)
                long += count
    
    return long

def dfs(lands,i,j):
    m = len(lands)
    n = len(lands[0])

    if (i == 0 or j ==0 or i >= m or j >= n or lands[i][j] == "0"):
        return 1
    if lands[i][j] == "2":
        return 0
    # 访问过的地方标记为2，说明已经访问过
    lands[i][j] = "2"
    # 以该点的上下左右方向进行递归
    return dfs(lands,i+1,j) + dfs(lands,i-1,j)+dfs(lands,i,j+1) +dfs(lands,i,j-1)