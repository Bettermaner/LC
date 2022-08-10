# 1.字符串无重复的全排列
    # 现在有字符串 abc ，我们需要列出它的全排列可能情况。
    # 对于字符串的第一个，也就是第0位字符 a，我们需要将字符串之后的，包括它本身在内的所有字符都与之交换，那么我们可以得到三组不同的字符串组合 {abc, bac, cba}。
    # 对1中得到的三个字符串组合 {abc, bac, cba}，重复1的过程，不过需要注意的是，这时是从第1位字符开始。举个栗子，对于 abc 来说 ，此时它的第1位字符是 b，那么需要将 b 之后的字符包括它本身与之交换，即需要交换两次 b <=> b, b <=> c，那么得到两组不同的字符串组合 {abc, acb}。
    # 对于2中得到的字符串组合，重复以上的过程，此时其实已经遍历到最后一个字符了，不做交换也可以，直接将字符串本身输出即可。这时我们就得到了所有的排列组合可能性。
class object :

    def __init__(self):
        self.result = []

    def per(self,strings):
        if len(strings) == 0:
            return self.result

        begin = 0
        end = len(strings)

        # 字符串转化成list
        strings = list(strings)

        self.sper(strings,begin,end)
        return self.result


    def sper(self,strings,begin,end):
        if begin == end:
            self.result.append("".join(strings))

        for i in range(begin,end):
            # 交换字符
            strings[begin],strings[i] = strings[i],strings[begin]
            # 递归
            self.sper(strings,begin+1,end)
            # 由于上一步操作对string进行了变化，需要 恢复原始的排列
            strings[begin],strings[i] = strings[i] ,strings[begin]


o = object()
print(o.per('abc'))