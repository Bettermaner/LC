from requests import head


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_node(phead,val):
    "给定单向链表的头指针和一个要删除的节点的值,定义一个函数删除该节点.返回删除后的链表的头节点"
    if not phead :
        return None
    pre = ListNode(-1)
    pre.next = phead
    tmp = pre
    cur = phead


    while cur:
        if cur.val == val:
            pre.next = cur.next
        pre = pre.next
        cur = cur.next
    return tmp.next 