def print_tree_from_bottom(phead):
    "不分行从上往下打印出二叉树的每个节点，同层节点从左至右打印"

    #解题思路： 辅助队列 先进先出思想
    res = []
    queue = []
    if not phead:
        return res

    queue.append(phead.val)

    while queue:
        # 先进先出原则，每次取出最先放进去的节点，重复依次取，直至没有
        root = queue[0]
        queue = queue[1:]

        res.append(root.val)

        left = root.left
        right = root.right
        if left:
            queue.append(left)
        if right:
            queue.append(right)

    return res