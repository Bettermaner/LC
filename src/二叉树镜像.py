def mirror(phead):
    "操作给定的二叉树，将其变换为源二叉树的镜像。"
    # 解题思路 递归

    if not phead:
        return None

    # 左右节点互换
    phead.left, phead.right = phead.right, phead.left

    mirror(phead.left)
    mirror(phead.right)

    return phead
