# 给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。


def dfs(root,res):
    if not root:
        return 

    res.append(root)
    dfs(root.left)
    dfs(root.right)

def func(root):
    res = []
    # 前序遍历
    dfs(root,res)

    n = len(res)

    head = res[0]
    for i in range(1,n):
        pre ,cur = res[i-1],res[i]
        pre.left = None
        pre.right = cur

    return head