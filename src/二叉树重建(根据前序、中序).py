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


# 通义大模型版本

# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]

# 方法1 : 递归       
# 时间复杂度	O(n²)（最坏情况）
# 空间复杂度	O(n²)（最坏情况）

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



# 方法2 : 哈希表+ 递归栈      
# 每个节点都会被访问一次，哈希表用于快速定位根节点位置。
# 所以总时间复杂度为：O(n)
# 使用了一个哈希表存储中序遍历的索引，空间复杂度为 O(n)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # 哈希映射：用于快速查找中序遍历中根节点的位置
        index_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0  # 指向前序遍历的指针

        def helper(left, right):
            # 当左边界大于右边界时，说明子树为空
            if left > right:
                return None

            # 当前子树的根节点是前序遍历当前指向的值
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)

            # 在中序遍历中找到根的位置，划分左右子树
            index = index_map[root_val]

            # 前序指针后移
            self.pre_idx += 1

            # 构建左子树
            root.left = helper(left, index - 1)
            # 构建右子树
            root.right = helper(index + 1, right)

            return root

        return helper(0, len(inorder) - 1)