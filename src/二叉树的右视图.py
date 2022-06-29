# 解题思路:
    # 递归
def right_graph(root):
    result = []
    if not root:
        return result

    queue = []
    queue.append(root)
    result.append(root.val)

    while queue:
        tmp_right = []

        for node in queue:
            if node.right:
                tmp_right.append(node.right)
            if node.left:
                tmp_right.append(node.left)
        if tmp_right:
            result.append(tmp_right[0])
        queue = tmp_right

    return result