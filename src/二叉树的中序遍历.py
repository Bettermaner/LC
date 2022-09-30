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