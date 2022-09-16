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