# 解题思路
    # 1.将链表按照，奇数节点与偶数节点分成两个链表
    # 2. 将偶数节点反转，变成升序排列
    # 3. 将两个链表从小到大合并起来
    
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def func(root):
    head1,head2 = split_list(root)

    reverse_head2 = reverse_list(head2)

    merge_root = merge_list(head1,reverse_head2)

    return merge_root

def split_list(root):
    cur1 = None
    cur2 = None
    
    count = 1
    while root:
        if count % 2 == 1:
            if cur1:
                cur1.next = root
                cur1 = cur1.next
            else:
                cur1 = root
                head1 = cur1
        else:
            if cur2: 
                cur2.next = root
                cur2 = cur2.next 
            else:
                cur2 = root
                head2 = cur2

        root = root.next
        count += 1
    cur1.next = None
    cur2.next = None
    return head1,head2

def reverse_list(root):
    if not root or not root.next:
        return root

    pre = None
    cur = root
    while cur:
        mid = cur.next
        cur.next = pre
        pre = cur
        cur = mid
    
    return cur
        
def merge_list(root1,root2):
    node = Node()
    head = node

    while root1 and root2:
        if root1.val >= root2.val:
            head.next = root2
            root2 = root2.next
        else:
            head.next = root1
            root1 = root1.next
        head = head.next

    if root1:
        head.next = root1

    if root2:
        head.next = root2

    return node.next