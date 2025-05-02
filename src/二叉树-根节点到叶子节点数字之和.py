# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：

# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。

# ✅ 解法思路
# 我们可以使用 深度优先搜索（DFS） 遍历整棵树：

# 每次递归时传入当前路径形成的数字。
# 当到达叶子节点时，将当前路径值加入总和。
# 最后返回所有路径值的总和。

# 时间复杂度	O(n)	每个节点访问一次
# 空间复杂度	O(h)	h 是树的高度，递归栈的空间


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.total = 0  # 全局变量保存总和

        def dfs(node, current_sum):
            if not node:
                return
            
            current_sum = current_sum * 10 + node.val  # 更新当前路径数字

            # 如果是叶子节点，累加到 total
            if not node.left and not node.right:
                self.total += current_sum
                return

            # 继续递归左右子树
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

        dfs(root, 0)
        return self.total
    
# 示例：

# 输入：root = [1,2,3]

# 输出：25

# 解题思路
    # 递归


def func(root):

    if not root:
        return 0

    total = dfs(root,0)
    return total


def dfs(root,total):
    if not root:
        return 0

    total = total * 10 + root.val

    if not root.left and not root.right:
        return total

    else:
        return dfs(root.left,total) + dfs(root.right,total)