# 给你一棵二叉树的根节点 root ，返回树的 最大宽度 。

# 树的 最大宽度 是所有层中最大的 宽度 。

# 每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。
# 将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。

# 输入：root = [1,3,2,5,3,null,9]
# 输出：4
# 解释：最大宽度出现在树的第 3 层，宽度为 4 (5,3,null,9) 。


# ✅ 解题思路：BFS + 编号法（类似完全二叉树编号）
# 我们可以使用 广度优先搜索（BFS），并给每个节点分配一个类似于完全二叉树结构中的位置编号：

# 根节点编号为 1
# 左子节点编号为 2 * i
# 右子节点编号为 2 * i + 1
# 这样每层最左边节点编号为 left，最右边节点编号为 right，那么该层的宽度为 right - left + 1


# 时间复杂度O(n **2)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def widthOfBinaryTree(root: TreeNode) -> int:
    if not root:
        return 0
    
    max_width = 0
    queue = [(root, 0)]  # 初始化时将根节点和其索引加入队列
    
    while queue:
        level_length = len(queue)
        _, first_index = queue[0]  # 当前层最左边的节点索引
        last_index = queue[-1][1]  # 当前层最右边的节点索引
        
        max_width = max(max_width, last_index - first_index + 1)
        
        for _ in range(level_length):
            node, index = queue.pop(0)  # 手动从列表头部弹出元素
            
            # 计算子节点的索引并加入队列
            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))

    return max_width