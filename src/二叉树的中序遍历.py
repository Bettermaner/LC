# 解题思路
    # 递归

def dfs(root,res):

    if not root:
        return 

    dfs(root.left,res)
    res.append(root.val)
    dfs(root.right,res)


def func(root):
    res = []
    dfs(root,res)
    
    return res

# 非递归（栈）
# 中序遍历
def in_order_func(root):

    res = []
    tmp = root
    stack = []

    while stack or tmp:
        while tmp:
            stack.append(tmp)
            tmp = tmp.left

        tmp = stack.pop()
        res.append(tmp.val)
        tmp = tmp.right

    return res

# 前序遍历
def pre_order_func(root):

    stack  =[root]
    res = []

    while stack:
        tmp = stack.pop()
        res.append(tmp.val)
        # 这里需要注意，这里要先把右节点放到栈里面，因为是先进后出
        if tmp.right:
            stack.append(tmp.right)
        if tmp.left:
            stack.append(tmp.left)

    return res 



# 通义大模型版本
# 方法	时间复杂度	空间复杂度
# 递归方法	O(n)	最坏 O(n)，平均 O(log n)
# 迭代方法（使用栈）	O(n)	最坏 O(n)，平均 O(log n)
# Morris遍历	O(n)	O(1)

#1. 迭代方法模拟了递归调用的过程，使用一个显式的栈来跟踪要访问的节点。
def inorderTraversal(root: TreeNode):
    stack, res = [], []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        res.append(current.val)
        current = current.right
    return res

# 2.Morris遍历是一种不需要额外空间的遍历方法，它通过修改树的结构来创建临时链接，从而在遍历完成后恢复原始结构。
def inorderTraversal(root: TreeNode):
    res = []
    current = root
    while current:
        if current.left is None:
            res.append(current.val)
            current = current.right
        else:
            # 找到current左子树的最右侧节点
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if predecessor.right is None:
                # 创建临时链接
                predecessor.right = current
                current = current.left
            else:
                # 移除临时链接并访问节点
                predecessor.right = None
                res.append(current.val)
                current = current.right
    return res