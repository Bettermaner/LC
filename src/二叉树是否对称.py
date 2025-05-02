# 这种方法的时间复杂度为 O(n)，其中 n 是树中节点的数量，
# 因为每个节点都会被访问一次。空间复杂度取决于递归调用的深度，最坏情况下为 O(h)，其中 h 是树的高度。

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


# 通义大模型版本
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    
    def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
    
    return isMirror(root.left, root.right)