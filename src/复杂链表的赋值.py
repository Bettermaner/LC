
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

def clone(phead):
    "输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。"
    if not phead :
        return phead

    # 解题思路： 双指针
    cur = phead

    # 将链表中的每一个节点都深拷贝一份，并放在节点的后面相邻的位置.
    while cur:
        clone = RandomListNode(cur.label)
        clone.next = cur.next
        cur.next = clone
        cur = clone.next

    cur = phead
    clone = phead.next

    # 记录当前拷贝节点的起始节点
    res = phead.next

    # 使用两个指针，一个指向原起始节点的位置，一个指向原始节点后一位拷贝的节点的位置
    # 两个指针每次移动两格。
    # 并将拷贝节点的random节点连接上
    while cur:
        if not cur.random :
            clone.random = None
        else:
            clone.random = cur.random.next
        
        if clone.next:
            clone = clone.next.next

        # 由于对每个节点进行了拷贝，只要cur存在，cur.next不会为空
        cur = cur.next.next


    # 将链表拆分成两个链表，并找出拷贝的链表
    cur = phead
    clone = phead.next
    while cur:
        cur.next = clone.next

        if clone.next:
            clone.next = clone.next.next

        clone = clone.next

        cur = cur.next

    return res

    
