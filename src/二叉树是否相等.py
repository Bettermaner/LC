

# 深度搜索

def run(phead1,phead2):

    if phead1.val == None and phead2.val == None:
        return True

    if phead1.val != phead2.val:
        return False

    if phead1.left.val != phead2.left.val:
        return False
    if phead1.right.val != phead2.right.val:
        return False

    return run(phead1.left,phead2.left) & run(phead1.right,phead2.right)


# 广度搜索
# 时间复杂度 o(min(m,n))
# 空间复杂度 o(min(m,n))

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null) {
            return false;
        }
        Queue<TreeNode> queue1 = new ArrayDeque<TreeNode>();
        Queue<TreeNode> queue2 = new ArrayDeque<TreeNode>();
        queue1.offer(p);
        queue2.offer(q);
        while (!queue1.isEmpty()) {
            TreeNode node1 = queue1.poll();
            TreeNode node2 = queue2.poll();
            if (node1.val != node2.val) {
                return false;
            }
            TreeNode left1 = node1.left, right1 = node1.right, left2 = node2.left, right2 = node2.right;
            if (left1 == null ^ left2 == null) {
                return false;
            }
            if (right1 == null ^ right2 == null) {
                return false;
            }
            if (left1 != null) {
                queue1.offer(left1);
                queue2.offer(left2);
            }
            if (right1 != null) {
                queue1.offer(right1);
                queue2.offer(right2);
            }
        }
        return true;
    }
}