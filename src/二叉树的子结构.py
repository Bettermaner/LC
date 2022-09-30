def has_sub_tree(phead1, phead2):
    "输入两棵二叉树A，B，判断B是不是A的子结构。（我们约定空树不是任意一个树的子结构）"
    # 解题思路： 递归

    # 如果B树为空，不会是任务树的子结构
    if not phead2:
        return False
    # 如果A树为空，B树不为空，则说明不是子结构
    if not phead1 and phead2:
        return False

    flag = False
    if phead1.val == phead2.val:
        flag = is_sub_tree(phead1, phead2)

    if not flag:
        # 如果主节点不存在子结构，再看左子树是否存在
        flag = has_sub_tree(phead1.left, phead2)

    if not flag:
        # 如果左子树不存在子结构，再看右子树是否存在
        flag = has_sub_tree(phead1.right, phead2)

    return flag


def is_sub_tree(root1, root2):
    if not root2:
        return True

    if not root1 and root2:
        return False

    if root1.val == root2.val:
        return is_sub_tree(root1.left, root2.left) and is_sub_tree(root1.right, root2.right)

    else:
        return False
