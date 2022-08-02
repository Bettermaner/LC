# 解题思路
    # 双指针
    # 分别使用两个指针遍历两个链表到末尾，判断两个指针末尾的节点是否相同
    # 如果相同说明有交叉，否则则没有交叉

    # 若有交叉，则重头开始遍历，长的链表先走 L1-L2步
    # 再两个指针同时走，每走一步判断是否相等，相等时，则是交叉点

def func(phead1,phead2):
    if not phead1 or  not phead2:
        return None
    
    cur1 = phead1
    p1_length = 0
    cur2 = phead2
    p2_length = 0

    while cur1.next:
        p1_length += 1
        cur1 = cur1.next

    while cur2.next:
        p2_length += 1
        cur2 = cur2.next

    if cur1 != cur2:
        return None

    if p1_length >= p2_length:
        t = p1_length - p2_length
        b_phead = phead1
        s_phead = phead2
    else:
        t = p2_length - p1_length
        b_phead = phead2
        s_phead = phead1

    while t:
        b_phead = b_phead.next
        t -=1
    
    while b_phead != s_phead:
        b_phead = b_phead.next
        s_phead = s_phead.next

    return b_phead

    
    



    