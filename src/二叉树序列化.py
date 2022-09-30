class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution:
    "二叉树序列化与反序列化"

    # 解题思路：中旬遍历递归，
    # 按照根，左，右的方式，拼接字符串
    # 然后按照这个顺序重新组件二叉树

    def __init__(self):
        self.index = 0
        self.s = ""

    def Serialize(self, root):
        phead = root
        if not phead:
            return ""
        self.ser(phead)
        return self.s

    def ser(self, root):
        if not root:
            return self.s

        self.s += str(root.val) + "!"

        if root.left:
            self.ser(root.left)
        else:
            self.s += "#!"

        if root.right:
            self.ser(root.right)
        else:
            self.s += "#!"

        return self.s

    def Deserialize(self, s):
        string = s
        if not string:
            return None

        array = string.split("!")
        return self.deser(array)

    def deser(self, array):

        if array[self.index] == "#":
            self.index += 1
            return

        # 先找出根节点
        root = TreeNode(int(array[self.index]))
        # 向前移一步
        self.index += 1
        # 再找左节点
        root.left = self.deser(array)

        # 最后找右节点
        root.right = self.deser(array)

        return root
