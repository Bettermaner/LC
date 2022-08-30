# 给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。
# 如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

# 解题思路
    # 蓄水池采样方式
    # 在n个数中等概率取m个数，怎么取？

    # 我们维持m大小的池子，

    # 当接收第i个数时，i小于m，则直接放到池子中，
    # 当i>=m时，则在[0,i]产生一个随机数d，若d落在[]0,m - 1]范围内，则用接收到的第i个数替换蓄水池中第d个数
    # 反复2

    # 在这里 m= 1
    # 随机一个随机数(random(1+K))，有1/(1+K)的概率，使用新数替换被选中的数值，自然就有(K/(1+k))的概率不被选中，自然，每个数字被选中的概率又都一样了。
    # 举个例子，第八位数字在总共十个数字中被选中的概率：
    # 如果第八位被选中，那就是第八次被选中，且第九次和第十次没有被替换，概率分别是1/8、8/9、9/10。相乘之后就是1/1
import random

class obj:

    def __init__(self,head):
        self.head = head

    
    def get_random(self):
        res = self.head.value
        head = self.head
        index = 0

        i = 1
        while head:
            random_index = random.randint(i)
            if random_index == index:
                res = head.value
            head = head.next
            i += 1
            
        return res
        