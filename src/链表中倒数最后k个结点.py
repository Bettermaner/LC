def find_k(phead, k):
    "输入一个长度为 n 的链表，设链表中的元素的值为 ai ，返回该链表中倒数第k个节点。"
    # 如果该链表长度小于k，请返回一个长度为 0 的链表。
    if not phead:
        return None

    # 解题思路,双指针
    # 先使用快指针走k步，然后慢指针开始走,让快慢指针之间保持k个距离。
    # 然后两个指针一起走，直至快指针到达末尾，取出慢指针的位置即可

    fast = phead
    slow = phead

    fast_step = 0
    while fast and fast_step < k:
        fast = fast.next
        fast_step += 1

    if fast_step < k:
        return None

    while fast:
        fast = fast.next
        slow = slow.next

    return slow
