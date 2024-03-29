# 给定一个正整数 n ，输出外观数列的第 n 项。

# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1 
# 描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
# 描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
# 描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
# 描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"

# 解题思路
    # 双指针遍历

def func(n):
    
    res = "1"
    for i in range(n-1):

        left = 0
        right = 0
        cur = ""

        while right < len(res) :
            while right < len(res) and res[left] == res[right]:
                right += 1

            cur += str(right-left) + res[left]
            left = right

        res = cur
    return res

print(func(6))