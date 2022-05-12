def reverse_list(phead):

    if not phead:
        return None

    if not phead.next:
        return phead

    # 左指针
    head = phead
    # 中间指针
    mid = phead.next
    # 右指针
    right = mid.next

    # 首先让起始点指向空,因为它将反转成最后一个节点
    head.next = None

    while right:

        # 每次循环保证 中间指针指向了左指针

        # 第一步 中间指针指向左指针
        mid.next = head
        # 第二步 左指针向前走一步,移到中间指针的位置
        head = mid
        # 第三步 中指针向前走一步,移到右指针的位置
        mid = right
        # 第四步 右指针向前走一步
        right = right.next

        # 四步下来，相当于整体指针向前移了一步。

    # 循环完后,右指针指向为空，说明此时中间指针已到达最顶部,再将中间指针指向左指针,完成反转
    mid.next = head
    return mid
