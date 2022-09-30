# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
# 同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

# 路径和 是路径中各节点值的总和。

# 给你一个二叉树的根节点 root ，返回其 最大路径和 

# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
class obj:

    def __init__(self):
        self.max_value = float('-inf')

    def func(self,root):

        if not root:
            return 0

        # 递归计算左右子节点的最大贡献值
        # 只有在最大贡献值大于 0 时，才会选取对应子节点
        left_gain = max(self.func(root.left),0)
        right_gain = max(self.func(root.right),0)

        #节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
        path_sum_value = root.val + left_gain + right_gain

        self.max_value = max(path_sum_value,self.max_value)

        # 返回节点的最大贡献值
        return root.val + max(left_gain,right_gain)

    def run(self,root):
        self.func(root)
        return self.max_value