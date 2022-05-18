def lowest_common_ancestor_binary_tree(phead,p,q):
    "二叉搜索树的最近公共祖先,注:一个节点也可以是它自己的祖先"
    
    # 解题方法: 递归
    # 解题思路:
        # 1.首先判断phead 是否为空节点,空树没有公共祖先
        # 2.判断p,q与phead根节点的大小,如果p,q分别在根节点的两边,说明phead就是最近公共祖先
        # 3.如果p,q都小于根节点,说明p,q都在根节点左边, 则递归左子树
        # 4.如果p,q都大于根节点,说明p,q都在根节点右边, 则递归右子树
    if not phead:
        return -1

    if (p >= phead.val and q <= phead.val) or (q >= phead.val and p <= phead.val):

        return phead.val

    elif (p >= phead.val and q >= phead.val):

        return lowest_common_ancestor_binary_tree(phead.right,p,q)
    
    elif (p <= phead.val and q <= phead.val):

        return lowest_common_ancestor_binary_tree(phead.left,p,q)