def merge_list_sort(phead1,phead2):
    "合并两个排序的链表"
    if not phead1:
        return phead2
    if not phead2:
        return phead1

    new_head = phead2 if phead1.val > phead2.val else phead1

    tmp1 = phead1
    tmp2 = phead2

    if new_head == phead1:
        tmp1 = tmp1.next
    else:
        tmp2 = tmp2.next
    
    pre_head = new_head

    while tmp1 and tmp2:

        if tmp2.val < tmp1.val:
            pre_head.next = tmp2
            pre_head = tmp2
            tmp2 = tmp2.next

        else:
            pre_head.next = tmp1
            pre_head = tmp1
            tmp1 = tmp1.next

    if tmp1:
        pre_head.next = tmp1
    else:
        pre_head.next = tmp2
    return new_head
