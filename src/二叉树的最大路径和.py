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
    



# 通义大模型跑出

# 🧠 解题思路
# 1. 关键点分析：
# 每个节点只能经过一次。
# 路径可以是任意两个节点之间的路径（不一定过根）。
# 每个节点都有可能成为“最高点”（即路径在该节点处拐弯）。
# 2. 如何用递归解决？
# 我们使用后序遍历的方式，对每个节点：

# 计算 左子树的最大贡献值（如果大于0才取）
# 计算 右子树的最大贡献值（如果大于0才取）
# 当前路径的最大值 = 当前节点值 + 左子树贡献 + 右子树贡献
# 更新全局最大路径和
# 返回当前节点能向上提供的最大路径和：当前节点值 + max(左贡献, 右贡献)

# ⏱️ 时间复杂度 & 空间复杂度
# 时间复杂度：O(n)，每个节点只访问一次。
# 空间复杂度：O(h)，h 是树的高度，递归栈的空间。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # 初始化最大路径和为负无穷
        self.max_sum = float('-inf')
        
        def gain(node):
            if not node:
                return 0
            
            # 递归计算左右子节点的最大贡献值
            left_gain = max(gain(node.left), 0)   # 如果小于0就不要了
            right_gain = max(gain(node.right), 0)
            
            # 当前节点作为“最高点”的路径和
            current_max = node.val + left_gain + right_gain
            
            # 更新全局最大路径和
            self.max_sum = max(self.max_sum, current_max)
            
            # 返回当前节点能给父节点的最大路径和
            return node.val + max(left_gain, right_gain)
        
        gain(root)
        return self.max_sum