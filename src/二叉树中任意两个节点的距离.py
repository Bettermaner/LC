# 解题思路
    # 先找出最近公共祖先
    # 两个节点的距离等于 dis(root,node1) + dis(root,node2)- 2 * dis(root,公共祖先)

# 计算root到指定节点的距离
def dis(root,node):
    if not root: 
        return -1
    if root == node:
        return 0

    distance = dis(root.left,node)
    if distance == -1:
        distance = dis(root.right,node)

    if distance != -1:
        return distance + 1
        
    return -1
