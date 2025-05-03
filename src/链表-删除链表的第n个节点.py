# 给定一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]



# 解题思路
# 要解决这个问题，我们可以使用 双指针技巧 来高效地找到并删除链表的倒数第 n 个节点。这种方法只需要遍历链表一次
# 因此时间复杂度为 O(L)，其中 L 是链表的长度。
# 使用两个指针：first 和 second。
# 初始化：让 first 指针先向前移动 n 步，然后同时移动 first 和 second 直到 first 到达链表的末尾。此时，second 将指向需要删除节点的前一个节点。
# 处理边界情况：如果要删除的是头节点（即 n 等于链表的长度），可以通过检查 first 是否在初始化后立即到达末尾来处理。

# 时间复杂度与空间复杂度分析
# 时间复杂度: O(L)，其中 L 是链表的长度。我们只遍历了链表一次。
# 空间复杂度: O(1)，因为我们只用了常数级别的额外空间。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # 创建一个哑结点(dummy node)，它的next指向head
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy
    
    # 让第一个指针先走n+1步，这样第二个指针就能停在目标节点的前一个位置
    for _ in range(n + 1):
        first = first.next
    
    # 同时移动两个指针直到第一个指针到达链表末尾
    while first:
        first = first.next
        second = second.next
    
    # 删除倒数第n个节点
    second.next = second.next.next
    
    # 返回结果链表的头结点
    return dummy.next