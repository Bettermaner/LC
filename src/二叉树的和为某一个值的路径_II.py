def find_path(phead,target):
    "输入一颗二叉树的根节点root和一个整数expectNumber，找出二叉树中结点值的和为expectNumber的所有路径。"
    # 1.该题路径定义为从树的根结点开始往下一直到叶子结点所经过的结点
    # 2.叶子节点是指没有子节点的节点
    # 3.路径只能从父节点到子节点，不能从子节点到父节点
    # 4.总节点数目为n

    res = []
    path = []
    # 解题思路：递归
    def dfs(root,target):

        if not root :
            return
        path.append(root.val)
        # 每到一个节点就是让 target 减一下
        target -= root.val

        # 当节点中没有左右节点,并且target此时为0时，说明满足条件
        if not root.left and not root.rigt and target == 0:
            tmp = path.copy()
            res.append(tmp)

        # 递归左子树，右子树
        dfs(root.left,target)
        dfs(root.right,target)

        # 很关键的一步，每次对当前节点的左右子树遍历完毕后，需要把当前节点从数组中去除，保证其他节点可以重新使用
        path.pop()
    dfs(phead,target)

    return res



class Solution:
    def pathTarget(self, phead: Optional[TreeNode], target: int) -> List[List[int]]:
        res = []
        path = []
        # 解题思路：递归
        def dfs(root,target):

            if not root :
                return
            path.append(root.val)
            # 每到一个节点就是让 target 减一下
            target -= root.val

            # 当节点中没有左右节点,并且target此时为0时，说明满足条件
            if not root.left and not root.right and target == 0:
                tmp = path.copy()
                res.append(tmp)

            # 递归左子树，右子树
            dfs(root.left,target)
            dfs(root.right,target)

            # 很关键的一步，每次对当前节点的左右子树遍历完毕后，需要把当前节点从数组中去除，保证其他节点可以重新使用
            path.pop()
        dfs(phead,target)

        return res