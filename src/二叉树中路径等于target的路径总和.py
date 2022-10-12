# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。

# 解题思路
    # 深度优先搜索
    

def dfs(root,target):
    if not root:
        return 0

    ret = 0
    if target == root.val:
        ret += 1

    ret += dfs(root.left,target-root.val)
    ret += dfs(root.right,target-root.val)
    return ret


def func(root,target):

    if not root :
        return 0

    ret = dfs(root,target)
    ret += dfs(root.left,target)
    ret += dfs(root.right,target)

    return ret

    