

def delete_duplicate_in_list(phead):
    "在有序的链表中删除重复的数(只删重复的数,不删除数本身)"

    if not phead:
        return None

    # 只需要一个指针即可
    cur = phead

    while cur.next:
        # 当cur = cur.next,说明相邻两个节点重复
        if cur.val == cur.next.val:
            # 将cur.next指针指向下下个节点,相当于跳过了右侧重复的节点
            cur.next = cur.next.next

        else:
            # 当cur = cur.next,说明相邻两个节点不重复,指针向前移动一下,继续判断下一轮的cur与cur.next值
            cur = cur.next

    return phead
