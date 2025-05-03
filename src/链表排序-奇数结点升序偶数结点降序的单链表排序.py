# 解题思路
    # 1.将链表按照，奇数节点与偶数节点分成两个链表
    # 2. 将偶数节点反转，变成升序排列
    # 3. 将两个链表从小到大合并起来
    

# 通义大模型版本
# 解题思路
# 分离链表：首先我们需要将原链表拆分成两个子链表，一个包含所有奇数索引位置的节点（已按升序排列），另一个包含所有偶数索引位置的节点（已按降序排列）。
# 反转偶数链表：由于偶数索引位置的节点是按降序排列的，我们需要将其反转以获得按升序排列的节点序列。
# 合并两个有序链表：最后一步是将这两个有序链表（一个是原始的奇数索引部分，另一个是经过反转后的偶数索引部分）合并成一个新的按升序排列的链表。

# 这种方法确保了在 O(n) 时间复杂度和 O(1) 空间复杂度内完成任务，符合题目要求

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortOddEvenList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    # 分离奇数和偶数索引的节点
    odd_dummy = ListNode(0)
    even_dummy = ListNode(0)
    odd_tail = odd_dummy
    even_tail = even_dummy
    index = 1
    
    while head:
        if index % 2 == 1:
            odd_tail.next = head
            odd_tail = odd_tail.next
        else:
            even_tail.next = head
            even_tail = even_tail.next
        head = head.next
        index += 1
    
    odd_tail.next = None  # 防止形成环
    even_tail.next = None
    
    odd_head = odd_dummy.next
    even_head = even_dummy.next
    
    # 反转偶数链表
    prev = None
    current = even_head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    even_head = prev  # 反转后的新头节点
    
    # 合并两个有序链表
    dummy = ListNode(0)
    tail = dummy
    
    while odd_head and even_head:
        if odd_head.val < even_head.val:
            tail.next = odd_head
            odd_head = odd_head.next
        else:
            tail.next = even_head
            even_head = even_head.next
        tail = tail.next
    
    # 如果有剩余节点，直接连接
    if odd_head:
        tail.next = odd_head
    if even_head:
        tail.next = even_head
    
    return dummy.next

# 辅助函数：打印链表
def printList(node: ListNode):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next