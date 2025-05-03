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
    


# 通义大模型版本
# 🧠 方法解释
# 使用递归函数 validate(node, low, high) 来判断当前节点是否在合法范围内；
# 对于左子树来说，最大值不能超过当前节点；
# 对于右子树来说，最小值不能低于当前节点；
# 如果任何一层不满足条件，直接返回 False。

# 时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点最多访问一次。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    # 使用辅助函数来进行递归检查
    def is_valid(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        
        # 检查当前节点值是否在允许范围内
        if node.val <= lower or node.val >= upper:
            return False
        
        # 递归检查左右子树
        return (is_valid(node.left, lower, node.val) and
                is_valid(node.right, node.val, upper))
    
    return is_valid(root)