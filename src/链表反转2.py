# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
# 请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。


# 解题思路
# 我们可以使用 头插法 或者 三指针迭代法 来实现。下面是推荐的解法：

# ✅ 标准做法：头插法 + 虚拟头节点
# 创建虚拟头节点 dummy 指向 head。
# 找到 left 前面的那个节点 pre。
# 使用头插法将 left 到 right 的节点逐个插入到 pre 后面。
# 返回 dummy.next。
# 这种方式不需要额外空间，且时间复杂度为 O(n)。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy

    # Step 1: 找到 left 前一个节点
    for _ in range(left - 1):
        pre = pre.next

    # Step 2: 定义当前节点 curr 和后续节点 cur_next
    curr = pre.next

    # Step 3: 头插法反转 left 到 right 的节点
    for _ in range(right - left):
        cur_next = curr.next
        curr.next = cur_next.next
        cur_next.next = pre.next
        pre.next = cur_next

    return dummy.next