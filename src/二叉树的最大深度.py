# 解题思路
    # 递归

def func(root):
    if not root:
        return 0
    left_depth = func(root.left)
    right_depth = func(root.right)

    return max(left_depth,right_depth) + 1
    