# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]

# 解法
# 归并排序（递归法）

# 通过递归实现链表归并排序，有以下两个环节：
    # 分割 cut 环节： 找到当前链表中点，并从中点将链表断开（以便在下次递归 cut 时，链表片段拥有正确边界）；
    # 我们使用 fast,slow 快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。
    # 找到中点 slow 后，执行 slow.next = None 将链表切断。
    # 递归分割时，输入当前链表左端点 head 和中心节点 slow 的下一个节点 tmp(因为链表是从 slow 切断的)。
    # cut 递归终止条件： 当head.next == None时，说明只有一个节点了，直接返回此节点。

    # 合并 merge 环节： 将两个排序链表合并，转化为一个排序链表。
    # 双指针法合并，建立辅助ListNode h 作为头部。
    # 设置两指针 left, right 分别指向两链表头部，比较两指针处节点值大小，由小到大加入合并链表头部，指针交替前进，直至添加完两个链表。
    # 返回辅助ListNode h 作为头部的下个节点 h.next。
    # 时间复杂度 O(l + r)，l, r 分别代表两个链表长度。
    # 当题目输入的 head == None 时，直接返回None。

def func(head):

    if not head or not head.next:
        return head

    slow = head
    fast = head.next

    if fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    #找到了 中点 slow,并找出中点右边的部分
    mid = slow.next
    #找到了 中点 slow，将中点左边的部分截断
    slow.next = None

    left,right = func(head),func(mid)


    h = res = Node(-1)
    
    while left and right:
        if left.value > right.value:
            res.next = right
            right = right.next
        else:
            res.next = left
            left = left.next
        res = res.next

    res.next = left if left else right

    return h.next