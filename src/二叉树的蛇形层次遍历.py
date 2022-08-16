# 解题思路
    # 队列，先进先出原则
    # 另外一个数组，正序的时候将节点插入数组尾部，倒序的时候将节点插入数组头部。

def func(root):
    result = []
    if not root :
        return result

    queue = []
    queue.append(root)

    # 是否倒序
    flag = False

    while queue:

        size = len(queue)

        array = []
        for i in range(size) :
            node = queue.pop(0)

            if flag:
                array.append(node.val)
            else:
                array = [node.val] + array

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        
        flag = not flag
        result.append(array)

    return result