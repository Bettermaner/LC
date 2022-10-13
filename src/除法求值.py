# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，
# 其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

# 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

# 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。
# 如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

# 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

# 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]

# 解题思路
    # 并查集数据结构
    # 并查集这三个字，一个字代表一个意思。
    # 并（Union），代表合并
    # 查（Find），代表查找
    # 集（Set），代表这是一个以字典为基础的数据结构，它的基本功能是合并集合中的元素，查找集合中的元素
    # 并查集的典型应用是有关连通分量的问题
    # 并查集解决单个问题（添加，合并，查找）的时间复杂度都是O(1)O(1)
    # 因此，并查集可以应用到在线算法中

# 并查集结构
# class UnionFind:

#     def __init__(self):
#         """
#         记录每个节点的父节点
#         并查集跟树有些类似，只不过她跟树是相反的。在树这个数据结构里面，每个节点会记录它的子节点。在并查集里，每个节点会记录它的父节点
#         """
#         self.father = {}

#     def add(self,x):
#         """
#         添加新节点
#         当把一个新节点添加到并查集中，它的父节点应该为空
#         """
#         if x not in self.father:
#             self.father[x] = None

#     def merge(self,x,y,val):
#         """
#         合并两个节点
#         如果发现两个节点是连通的，那么就要把他们合并，也就是他们的祖先是相同的。这里究竟把谁当做父节点一般是没有区别的。
#         """
#         root_x,root_y = self.find(x),self.find(y)
        
#         if root_x != root_y:
#             self.father[root_x] = root_y

#     def is_connected(self,x,y):
#         """
#         判断两节点是否相连
#         """
#         return self.find(x) == self.find(y)


#     def find(self,x):
#         """
#         查找根节点
#         查找祖先的方法是：如果节点的父节点不为空，那就不断迭代。

#         路径压缩
#         并查集只是记录了节点之间的连通关系，而节点相互连通只需要有一个相同的祖先就可以了。
#         """
#         root = x

#         while self.father[root] != None:
#             root = self.father[root]

#         # 路径压缩
#         while x != root:
#             original_father = self.father[x]
#             self.father[x] = root
#             x = original_father
         
#         return root


class UnionFind:

    def __init__(self):
        """
        记录每个节点的父节点
        """
        self.father = {}
        self.value = {}

    def add(self,x):
        """
        添加新节点
        当把一个新节点添加到并查集中，它的父节点应该为空
        """
        if x not in self.father:
            self.father[x] = None
            self.value[x] = 1

    def merge(self,x,y,val):
        """
        合并两个节点
        如果发现两个节点是连通的，那么就要把他们合并，也就是他们的祖先是相同的。这里究竟把谁当做父节点一般是没有区别的。
        """
        root_x,root_y = self.find(x),self.find(y)
        
        if root_x != root_y:
            self.father[root_x] = root_y
            ##### 四边形法则更新根节点的权重
            self.value[root_x] = self.value[y] * val / self.value[x]

    def is_connected(self,x,y):
        """
        判断两节点是否相连
        """
        return x in self.value and y in self.value and self.find(x) == self.find(y)


    def find(self,x):
        """
        查找根节点
        查找祖先的方法是：如果节点的父节点不为空，那就不断迭代。

        路径压缩
        并查集只是记录了节点之间的连通关系，而节点相互连通只需要有一个相同的祖先就可以了。
        """
        root = x
        # 节点更新权重的时候要放大的倍数
        base = 1
        while self.father[root] != None:
            root = self.father[root]
            base *= self.value[root]
        
        while x != root:
            original_father = self.father[x]
            ##### 离根节点越远，放大的倍数越高
            self.value[x] *= base
            base /= self.value[original_father]
            #####
            self.father[x] = root
            x = original_father
         
        return root

def func(equations,values,queries):
    uf = UnionFind()

    for (a,b),val in zip(equations,values):
        uf.add(a)
        uf.add(b)
        uf.merge(a,b,val)

    n = len(queries)

    res = [-1] * n

    for i in range(n):
        (a,b) = queries[i]
        if uf.is_connected(a,b):
            t = uf.value[a] / uf.value[b]
            res[i] = t

    return res


print(func([["a","b"],["b","c"]], [2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))

