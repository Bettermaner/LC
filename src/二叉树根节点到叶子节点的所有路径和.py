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