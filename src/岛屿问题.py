# 解题思路
    # dfs递归

# 1. 岛屿数量

class Solution:
    def numIslands(self, lands: List[List[str]]) -> int:

        m = len(lands)
        n = len(lands[0])

        count = 0

        def dfs(lands, i, j):
            # 修改边界条件判断
            if i < 0 or j < 0 or i >= m or j >= n or lands[i][j] == "0":
                return 
            # 访问过的地方标记为0，说明已经访问过
            lands[i][j] = "0"
            # 以该点为中心向四周扩展
            dfs(lands, i - 1, j)
            dfs(lands, i + 1, j)
            dfs(lands, i, j - 1)
            dfs(lands, i, j + 1)
            
        for i in range(m):
            for j in range(n):

                if lands[i][j] == "1":
                    dfs(lands,i,j)
                    count += 1
        
        return count



# 2.岛屿的最大面积
class Solution:
    def maxAreaOfIsland(self, lands: List[List[int]]) -> int:
            
        m = len(lands)
        n = len(lands[0])


        def dfs(lands, i, j):
            if i < 0 or j < 0 or i >= m or j >= n or lands[i][j] == 0:
                return 0
            
            # 标记访问过的节点
            lands[i][j] = 0
            area = 1  # 当前格子计入面积
            
            # 累加四个方向上的面积
            area += dfs(lands, i - 1, j)
            area += dfs(lands, i + 1, j)
            area += dfs(lands, i, j - 1)
            area += dfs(lands, i, j + 1)

            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if lands[i][j] == 1:  # 使用整数1进行比较
                    area = dfs(lands, i, j)
                    max_area = max(area, max_area)
        
        return max_area


# 3.岛屿的周长
# 观察后发现，从陆地走到水域或者从陆地走向边界时，都会出现一条边，既为周长的一部分，依次统计即可
# 需要注意的是，当标记访问过的陆地时不能再使用0，会和水域混淆调，因此用2标记

class Solution:
    def islandPerimeter(self, lands: List[List[int]]) -> int:
        m = len(lands)
        n = len(lands[0])

        def dfs(lands,i,j):
            m = len(lands)
            n = len(lands[0])

            if (i < 0 or j < 0 or i >= m or j >= n or lands[i][j] == 0):
                return 1
            if lands[i][j] == 2:
                return 0
            # 访问过的地方标记为2，说明已经访问过
            lands[i][j] = 2
            # 以该点的上下左右方向进行递归
            return dfs(lands,i+1,j) + dfs(lands,i-1,j)+dfs(lands,i,j+1) +dfs(lands,i,j-1)


        long = 0
        for i in range(m):
            for j in range(n):
                if lands[i][j] == 1:
                    count = dfs(lands,i,j)
                    long += count
        
        return long