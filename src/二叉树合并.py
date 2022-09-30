# 解题思路
    # 递归
    # 当相同位置的节点都不为空，则把值相加返回新节点
    # 否则返回其中不为空的节点

def merge_tree(root1,root2):
    if not root1 and root2:
        return None
    if not root1:
        return root2
    if not root2:
        return root1

    root = Tree(root1.val+root2.val)
    root.left = merge_tree(root1.left,root2.left)
    root.right = merge_tree(root2.right,root2.right)
    return root