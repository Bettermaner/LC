def verify_sequence_of_bst(sequence):
    "输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回 true ,否则返回 false 。假设输入的数组的任意两个数字都互不相同。"
    # 二叉搜索树 特点：根节点左边节点都小于根节点，根节点右边节点都大于根节点
    # 解题思路: 分治
    # 后序遍历：左节点 -》 右节点 -》 根节点，所以序列最后一位是根节点

    # 空树不为二叉搜索树
    if not sequence:
        return False

    start_index = 0
    end_index = len(sequence) - 1

    def verify(sequence,start,end):
        # 当当前子树只有一个节点时，说明树已经到达底部，没有问题
        if start >= end:
            return True

        # 根节点
        root = sequence[end]

        # 首先找出右子树
        j = end -1 
        while j > start and sequence[j] > root:
            j -= 1

        # 再找左子树,如果左子树中有节点大于根节点，说明有问题
        i = start
        while i <= j:
            if  sequence[i] >= root:
                return False
            i += 1

        # 找出左右子树后，继续重复上面的操作，直至到树的底部

        return verify(sequence,0,j) and verify(sequence,j+1,end-1)
        
    return verify(sequence,start_index,end_index)

