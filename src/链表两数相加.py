# 将两个链表看成相同长度后，进行遍历，如果一个链表较短则在前面补0，如 987 + 23 = 987 + 023 = 1010
# 每一位计算的同时需要 考虑上一位的进位，并更新到前方的节点
# 如果遍历完毕，进位值为1，则在新链表前方加一个节点1

# 小技巧：对于链表问题，返回结果为头结点时，通常需要先初始化一个预先指针 pre，该指针的下一个节点指向真正的头结点head。

def func(phead1,phead2):

    # 进位值
    carray = 0

    pre = Node(0)

    cur = pre

    while phead1 or phead2:

        p1 = phead1.value if phead1 else 0
        p2 = phead2.value if phead2 else 0

        sum_p = p1 + p2 + carray

        carray = sum_p / 10
        p = sum_p % 10

        cur.next = Node(p)
        cur = cur.next

        if phead1:
            phead1 = phead1.next
        if phead2:
            phead2 = phead2.next 
            
        if carray == 1:
            cur.next = Node(carray)

    return pre.next 


# 通义大模型版本

# 时间复杂度: O(max(m, n))
# 其中 m 和 n 分别是两个链表的长度。我们只需要遍历一次较长的那个链表。

# 空间复杂度: O(max(m, n))
# 返回的结果链表长度最多为 max(m, n) + 1（可能最后多出一个进位）。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # 虚拟头节点，方便操作链表
    dummy = ListNode(0)
    current = dummy  # 当前指针用于构建新链表
    carry = 0  # 进位值

    # 只要有一个链表还没结束 或者 还有进位，就继续运算
    while l1 or l2 or carry:
        # 获取当前节点的值
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # 相加并处理进位
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # 创建新节点并连接
        current.next = ListNode(digit)
        current = current.next

        # 移动指针
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next