class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rebuild_binary_tree(pre,tin):
    "给定节点数为 n 的二叉树的前序遍历和中序遍历结果,请重建出该二叉树并返回它的头结点"
    # 算法思路: 递归
    # 解题思路: https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=265&tqId=39211&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D265&difficulty=undefined&judgeStatus=undefined&tags=&title=

    # 前序遍历, 根-> 左-> 右
    # 中序遍历, 左-> 根 -> 右
    # 后序遍历, 左-> 右 -> 根

    if not pre:
        return None

    # 根节点的值
    root_value = pre[0]
    # 创建当前的根节点
    root = TreeNode(root_value)

    # 根节点在中序遍历中的索引位置
    # 由于中序遍历, 左-> 根 -> 右,所以该索引左边数组为左子树的中序遍历,该索引右边为右子树的中序遍历
    # 还说明该左子树有 tin_root_index 个节点
    tin_root_index = tin.index(root_value)

    # root找对应的左子树与右子树
    root.left = rebuild_binary_tree(pre[1:tin_root_index+1],tin[:tin_root_index])
    root.right = rebuild_binary_tree(pre[tin_root_index+1:],tin[tin_root_index+1:])

    return root



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rebuild_binary_tree(preorder: list, inorder: list) -> TreeNode:
    if not preorder or not inorder:
        return None
    
    if len(preorder) != len(inorder):
        raise ValueError("Preorder and inorder lists must have the same length.")
    
    # 根节点的值
    root_value = preorder[0]
    # 创建当前的根节点
    root = TreeNode(root_value)
    
    # 根节点在中序遍历中的索引位置
    try:
        tin_root_index = inorder.index(root_value)
    except ValueError:
        raise ValueError("Root value from preorder not found in inorder list.")
    
    # 递归构建左右子树
    root.left = rebuild_binary_tree(preorder[1:tin_root_index + 1], inorder[:tin_root_index])
    root.right = rebuild_binary_tree(preorder[tin_root_index + 1:], inorder[tin_root_index + 1:])
    
    return root