
def ring_entrance_node(head):

    if not head:
        return None

    fast = head
    slow = head
    fast_step = 0
    slow_step = 0

    is_ring = False
    entrance_node = None
    ring_length = None

    # 从起点到环入口距离为a, 从a到相遇点距离为b，环的长度距离为c
    # 当两个指针相遇时满足： 2 *（a + b）= a + b + c  => c - b = a

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        fast_step += 2
        slow_step += 1
        # 如果相遇,说明有环
        if  fast == slow:
            is_ring = True
            ring_length = fast_step - slow_step
            break
    
    if not fast or not slow:
        return is_ring,entrance_node,ring_length

    # 起点到环入口的距离a = 从相遇点到环入口的距离 c - b
    fast = head 
    while fast != next:
        fast = fast.next
        slow = slow.next
    entrance_node = fast
    return is_ring,entrance_node,ring_length

