def ring_entrance_node(head):
    "链表中是否有环,入口环,环长度"

    is_ring = False
    entrance_node = None
    ring_length = None

    if not head:
        return is_ring, entrance_node, ring_length

    fast = head
    slow = head

    # 从起点到环入口距离为a, 从环入口到相遇点距离为b，环的长度距离为c,
    # n，m分别表示慢指针与快指针绕了几次环。
    # 当两个指针相遇时满足： 2 *（a + b + n* c）= a + b + m * c
    # a = (n - 2*m -1) * c + c -b

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        # 如果相遇,说明有环
        if fast == slow:
            is_ring = True
            break

    if not fast or not slow:
        return is_ring, entrance_node, ring_length

    # 即从起点到环入口的距离 a = x倍的环长度c + （c - b）,x可能为0
    # 所以如果快指针回到起点,慢指针在相遇点继续走，必定会在环入口相遇。
    fast = head
    # 快指针回到起点后，走的步数
    fast_step = 0

    # 环中的相遇点
    meet = slow
    # 在相遇后,慢指针在环中绕过的次数
    slow_ring_count = 0

    while fast != slow:
        fast = fast.next
        slow = slow.next
        if slow == meet:
            slow_ring_count += 1
        fast_step += 1

    # 入口节点
    entrance_node = fast
    tmp_entrance_node = fast

    # 从环入口a到相遇点的距离
    entrance_to_meet_len = 0
    while tmp_entrance_node != meet:
        tmp_entrance_node = tmp_entrance_node.next
        entrance_to_meet_len += 1

    # fast_step = slow_ring_count * c + (c -b)
    # 环长度 c = (fast_step + b) / (slow_ring_count + 1)
    ring_length = (fast_step + entrance_to_meet_len) / (slow_ring_count + 1)

    return is_ring, entrance_node, ring_length
