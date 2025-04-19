

# 搜索二叉树性质，左边节点小于根节点，右边节点大于根节点
def run(bst,m):

    result = -1
    
    while bst:
        if bst.value >= m: # 如果比m大，则在left节点继续找
            bst = bst.left
        else:
            result = bst.value # 否则就直接赋值
            bst = bst.right
            
    return result 