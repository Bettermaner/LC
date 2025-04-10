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