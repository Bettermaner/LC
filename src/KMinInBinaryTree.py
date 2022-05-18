class KMinInBinaryTree:

    def __init__(self) -> None:
        self.result = None

        # 记录从最左子树的左节点开始,中序遍历了多少次
        # 最左子树的左节点值最小,依次递增,递增到第k个则找到了第k小的数
        self.count = 0


    def k_min_binary_tree(self,phead,k):
        "二叉搜索树的第k个节点"

        # 二叉搜索树属于特殊的二叉树,根节点的左子树的值都小于根节点的值,根节点的右子树的值都大于根节点的值
        # 解题方法: 中序遍历 递归, 左 -> 根 -> 右,从数值左到右递增
        self.in_order(phead,k)
        if self.res:
            return self.res.val
        else:
            return -1

    def in_order(self,root,k):

        if not root or self.count > k:
            return 

        self.in_order(root.left,k)
        self.count += 1
        
        # 每次判断当前root节点是否遍历了k次,如果遍历了k次,说明到达了第k小的值
        if self.count == k:
            self.res = root

        self.in_order(root.right,k)
