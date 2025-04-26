class NextNodeBinaryTree:

    def next_node_binary_tree(self,phead):
        "给定一个二叉树其中的一个结点,请找出中序遍历顺序的下一个结点并且返回。注意,树中的结点不仅包含左右子结点,同时包含指向父结点的next指针相当于指向当前节点的上一个节点"
        if not phead:
            return None

        # 解题方法: 递归
        # 二叉树的递归，则是将某个节点的左子树、右子树看成一颗完整的树，那么对于子树的访问或者操作就是对于原树的访问或者操作的子问题，因此可以自我调用函数不断进入子树.
        # 解题思路
            # 1. 根据给出的当前节点反推找到二叉树的根节点
            # 2. 根据根节点递归获取二叉树的中序遍历
            # 3. 根据中序遍历找到给出的节点在中序遍历所处的索引位置
            # 4. 索引位置下一个节点就是中序遍历顺序的下一个结点

        # 根节点
        root = phead
        while root.next:
            root = root.next

        # 递归获取中序遍历
        self.in_order_list = []
        self.in_order(root)


        for i,value in enumerate(self.in_order_list):

            if value == phead and i + 1 < len(self.in_order_list):
                return self.in_order_list[i+1]

        else:
            return None

    def in_order(self,root):
        if not root:
            return
        # 中序遍历,左-> 根 -> 右
        self.in_order(root.left)
        self.n_order_list.append(root)
        self.in_order(root.right)





