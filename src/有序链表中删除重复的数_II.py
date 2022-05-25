class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_dulicate_in_list(phead):
    "在有序的链表中删除重复的数(重复的数与数本身都需要删除)"
    # 需要两个指针来完成

    if not phead:
        return None

    # 创建一个节点,专门来标记有序链表的起始位置
    head = ListNode(0)
    # 将head赋值给pre，pre进行移动
    pre = head
    # pre.next 指向phead链表中的第一个节点(起始节点位置)
    # 因为 head = pre,所以head.next=phead，head下一个始终指向phead链表中的第一个节点(起始节点位置)
    pre.next = phead
    # cur 专门标记phead链表当前所处的位置，刚开始也处于链表中的第一个节点(起始节点位置)
    cur = phead

    while cur:

        if cur.next and cur.val == cur.next.val:
            # 如果cur = cur.next，说明相邻的两个节点相等，指针向前移动一个,继续比较
            # 直至相邻的两个节点不相等,cur指针停止移动
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            # 这时将pre的指针指向相邻右边节点(与当前cur不相等的节点)上，说明跳过了所有重复的节点
            pre.next = cur.next
            # 这时将cur也向前移动一下,到与当前cur不相等的节点上
            cur = cur.next

        else:
            # 如果cur ！= cur.next，说明相邻的两个节点不重复，当前phead链表不改变,pre与cur都向前移动一下,继续判断下一轮的cur与cur.next值
            pre = pre.next
            cur = cur.next

    # head.next就表示了phead链表中的起始节点
    return head.next


# 注: 节点 = 节点.next 不会改变当前链表顺序,只会让当前指针向前移动
#     节点.next = 节点，会改变当前链表顺序
