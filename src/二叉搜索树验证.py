# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 解题思路
    # 中序遍历+递归
    # 中序遍历后，数字从小到大排列 
class obj:
    pre = float("-inf")

    def func(self,root):

        if not root:
            return True

        if not self.func(root.left):
            return False

        if root.val <= pre:
            return False

        pre = root.val

        return self.func(root.right)