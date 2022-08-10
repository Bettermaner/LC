# 解题思路:
    # 递归

from cgitb import reset


def left_graph(root):
    result = []
    if not root:
        return result

    queue = []
    queue.append(root)


    while queue:

        tmp_left = []

        for node in queue:
            if node.left:
                tmp_left.append(node.left)
            if node.right:
                tmp_left.append(node.right)
        if tmp_left:
            result.append(tmp_left[0])
        queue = tmp_left

    return result

        