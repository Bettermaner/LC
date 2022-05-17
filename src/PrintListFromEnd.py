def print_list_from_end(phead):
    "输入一个链表的头节点,按链表从尾到头的顺序返回每个节点的值"
    result = []

    if not phead:
        return result

    cur = phead

    while cur:
        result.append(cur.val)
        cur = cur.next
    
    result.reverse()

    return result