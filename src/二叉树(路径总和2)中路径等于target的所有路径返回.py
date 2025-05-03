# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

# 叶子节点 是指没有子节点的节点。

# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]


# 🧠 解题思路：DFS 深度优先搜索
# 我们可以使用 递归 DFS 来遍历这棵树：
# 从根节点开始，向下递归，记录当前路径；
# 如果当前是叶子节点，并且当前路径和等于 targetSum，就将这条路径加入结果中；
# 否则继续递归左右子树；
# 注意点：回溯时要弹出当前节点。


# 时间复杂度: O(n)，其中 n 是树中节点的数量。每个节点最多访问一次。
# 空间复杂度: O(h)，h 是树的高度（递归栈的空间 + 当前路径占用的空间）


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: TreeNode, targetSum: int) -> list[list[int]]:
    result = []
    
    def dfs(node, current_path, current_sum):
        if not node:
            return
        
        current_sum += node.val
        current_path.append(node.val)

        # 如果是叶子节点并且路径和等于 targetSum
        if not node.left and not node.right and current_sum == targetSum:
            result.append(list(current_path))  # 注意这里要复制一份路径

        # 继续递归左右子树
        dfs(node.left, current_path, current_sum)
        dfs(node.right, current_path, current_sum)

        # 回溯：把当前节点从路径中移除
        current_path.pop()
    
    dfs(root, [], 0)
    return result