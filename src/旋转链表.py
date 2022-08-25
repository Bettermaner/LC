# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

# 示例 1:

# 输入: 1->2->3->4->5->NULL, k = 2

# 输出: 4->5->1->2->3->NULL


def func(root,k):
    if not root:
        return None

    lenght = 0

    head = root
    # 遍历完链表，并记录链表长度
    while root:
        root = root.next
        lenght += 1

    # 链表首尾相连
    root.next = head

    # 如果操作次数k大于链表长度n就存在重复的操作，
    # 其中的整数*n个操作是互相抵消的。因此一共旋转的次数可以简化为k%n次，从而降低时间复杂度。 
    k = k % lenght

    # 继续遍历链表
    i = 0
    while i < lenght - k:
        root = root.next
        i += 1

    # 记录当前的起始点
    head = root.next

    # 断开此时的节点,断开环
    root.next = None

    return head
    