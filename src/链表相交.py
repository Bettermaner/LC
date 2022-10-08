# 给你两个单链表的头节点 headA 和 headB ，
# 请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
# 注意，函数返回结果后，链表必须 保持其原始结构 。


# 双指针
# 考虑构建两个节点指针 A​ , B 分别指向两链表头节点 headA , headB ，做如下操作：

# 指针 A 先遍历完链表 headA ，再开始遍历链表 headB ，当走到 node 时，共走步数为：
# a + (b - c)
# a+(b−c)

# 指针 B 先遍历完链表 headB ，再开始遍历链表 headA ，当走到 node 时，共走步数为：
# b + (a - c)
# b+(a−c)

# 如下式所示，此时指针 A , B 重合，并有两种情况：

# a + (b - c) = b + (a - c)
# a+(b−c)=b+(a−c)

# 若两链表 有 公共尾部 (即 c > 0) ：指针 A , B 同时指向「第一个公共节点」node 。
# 若两链表 无 公共尾部 (即 c = 0 ) ：指针 A , B 同时指向 null 。

class Solution:
    def getIntersectionNode(self, headA, headB):
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
