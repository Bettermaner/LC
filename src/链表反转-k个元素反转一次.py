# 解题思路
    # 使用多个指针完成
    # 保存四个指针，pre记录当前节点，start记录每个窗口的起始节点，end记录每个窗口的结束节点，next记录下个窗口的起始节点

def reverse_group_k(root,k):
    if not root:
        return None

    dummy = Tree(0)

    pre = dummy
    end = dummy

    dummy.next = root

    while end :
        i = 0
        while i < k and end:
            end = end.next
            i += 1
        if not end :
            break
        # 记录下一个窗口的起始节点
        next = end.next
        # 记录当前窗口的起始节点
        start = pre.next

        # 将当前窗口的end位置的节点，next指向null，后面做反转时好判断到哪里停止。
        end.next = None

        # 将当前指针指向反转后的起始节点。
        pre.next = reverse_list(start)

        # 经过反转后start节点目前在窗口的结束位置,将结束位置的next指向下一个窗口的起始位置，从而连接起来
        start.next = next

        pre = start
        end = start

    return dummy.next


def reverse_list(root):
    if not root:
        return None

    pre = None
    cur = root

    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre