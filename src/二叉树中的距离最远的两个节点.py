#解题思路:
    # 递归找出左子树的深的深度，右子树最深的深度
    # 左右子树的最深处的节点距离最大
class o:
    def __init__(self):
        self.max_depth = 0

    def max_depth_node(self,root):
        if not root:
            return 0
        left_max_depth = self.max_depth_node(root.left)
        right_max_depth = self.max_depth_node(root.right)

        if self.max_depth < left_max_depth + right_max_depth:
            self.max_depth = left_max_depth + right_max_depth

        # 需要把当前节点考虑进去，所以加1
        return max(left_max_depth,right_max_depth) + 1

    def get(self,root):

        self.max_depth_node(root)
        return self.max_depth