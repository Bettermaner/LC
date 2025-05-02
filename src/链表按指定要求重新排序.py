#输入：1->2->3->4->5->6->7

# 输出：1->7->2->6->3->5->4


# 解题思路
# 思路：

# 1. 将1->2->3->4->5->6->7分成：1->2->3 与 4->5->6->7，将后半部分逆序7->6->5->4

# 2. 合并1->2->3与7->6->5->4 为1->7->2->6->3->5->4

# 3. 划分：就是找到中间节点mid，作为后半部分的头节点（注意后半部分的节点数量会比前半部分多0个或者1个节点），这里引入了slow与fast两个外部变量，fast一次走2步，slow一次走一步，这样fast走完时，slow正好走了一半，从而找到中间节点，同时，还需引入slow_pre外部变量，作为slow的前一个节点，目的是为了找到中间节点的slow时，通过slow_pre.next = None的方式，断开链表，分成2个链表

# 4. 逆序：输入后半段的头节点，也就是mid，实现对链表逆序操作，可参考之前的文章，此处采用插入法逆序（链表逆序）

# 5. 合并：引入外部变量cur1, cur2用来操作两个链表，每个节点仍然是2次指针操作，但要注意，每节点指针操作结束后，需要将外部操作变量cur下移。最后当cur1遍历结束，即cur1.next为None时，跳出循环，将cur1.next指向cur2，cur2为最后一个节点。


def find_mid_node(head):

    if not head or not head.next:
        return head

    fast = head
    slow = head
    # 用于将两个链表分开
    slow_pre = head

    while not fast and not fast.next:
        slow_pre = slow
        slow = slow.next
        fast = fast.next.next

    # 将show_pre的next节点指向空，将一个链表变成两个链表
    slow_pre.next = None

    return slow


def reverse_list(head):
    if not head or  not head.next:
        return head

    cur = head 
    pre = None

    while cur.next:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre


def reorder(head):
    if not head or  not head.next:
        return head

    cur1 = head
    mid = find_mid_node(head)
    cur2 = reverse_list(mid)

    while cur1.next:

        tmp1 = cur1.next
        cur1.next = cur2
        cur1 = tmp1

        tmp2 = cur2.next
        cur2.next = cur1
        cur2 = tmp2

    cur1.next = cur2
    
    return head  
