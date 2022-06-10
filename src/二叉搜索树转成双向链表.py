class Solution:

    def __init__(self):
        self.head = None
        self.cur = None

    def covert(self,phead):
        "输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表"
        if not phead:
            return phead

        # 解题思路: 中序遍历,递归
        # 左 -》 根 -》 右，从小到大排列
        self.covert(phead.left)

        # 如果为空，说明遍历到最左边的节点，最小值。
        if not self.cur:
            self.cur = phead
            self.head = phead

        # 如果有值则双向赋值
        else:
            self.cur.right = phead
            phead.left = self.cur
            # 当前指针向前进一步
            self.cur = phead

        self.covert(phead.right)
        
        return self.head