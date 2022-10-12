# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
# 使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

# 提醒一下，二叉搜索树满足下列约束条件：

# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。

# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

# 解题思路
    # 根据二叉搜索树的特征，右中左深度遍历
    # 可以发现遍历到的第一个节点，是树中值最大的节点，转化成累加树，其节点的值还是其本身


class obj :

    def __init__(self) -> None:
        self.tmp = 0

    def func(self,root):

        self.dfs(root)

        return root

    def dfs(self,root):
        if not root:
            return 

        self.dfs(root.right)
        tmp += root.val
        root.val = tmp
        self.dfs(root.left)

