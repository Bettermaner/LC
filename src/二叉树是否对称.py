def is_symmetrical(phead):
    "给定一棵二叉树，判断其是否是自身的镜像（即：是否对称)"

    # 解题思路 递归
    if not phead:
        return True
    # 输入一个相同的二叉树镜像，比较，A树左节点是否等B树右节点
    phead1 = phead
    phead2 = phead

    flag = symmetrical(phead1, phead2)

    return flag


def symmetrical(root1, root2):

    if not root1 and not root2:
        return True
    elif not root1 and root2:
        return False
    elif root1 and not root2:
        return False
    if root1.val == root2.val:
        return symmetrical(root1.left, root2.right) and symmetrical(root1.right, root2.left)
    else:
        return False
