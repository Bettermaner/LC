# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。

# 解题思路一：
    # 深度优先搜索

# 时间复杂度：O(n)，其中 n 是树中节点的总数。每个节点最多访问一次。
# 空间复杂度：
# 最坏情况下是 O(h)，h 是树的高度（递归调用栈的深度）

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if not root:
        return False

    # 如果是叶子节点，判断是否满足 targetSum
    if not root.left and not root.right:
        return root.val == targetSum

    # 否则继续递归左右子树，看是否有一边能满足条件
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)
    



# 解题思路二：栈
# 这种方法通过显式地使用一个栈来保存遍历过程中的节点和当前路径的和，从而避免了递归调用带来的函数调用开销
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if not root:
        return False
    
    # 使用栈来保存(节点, 当前路径和)
    stack = [(root, root.val)]
    
    while stack:
        node, current_sum = stack.pop()
        
        # 如果到达叶子节点，检查路径和是否等于targetSum
        if not node.left and not node.right:
            if current_sum == targetSum:
                return True
        
        # 将右子节点加入栈
        if node.right:
            stack.append((node.right, current_sum + node.right.val))
        
        # 将左子节点加入栈
        if node.left:
            stack.append((node.left, current_sum + node.left.val))
    
    return False