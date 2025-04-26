# 给你一个字符串 s ，考虑其所有 重复子串 ：即，s 的连续子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。
# 返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 “” 
# 解题思路
    # 双指针加滑动窗口
    # 1.建立左右指针，左指针起始位置为0，右指针起始位置为1
    # 2.看左右指针构成的窗口中的字符是否在除左指针外的右侧区域有重复出现
    # 3.如果有重复出现，右指针则向右移动一位，再继续执行2的操作判断
    # 4.如果没有重复出现，左指针则向右移动一位，再继续执行2的操作判断 （当 左指针与右指针相等，右指针向右移动一位）
    # 5.重复上述操作，直至右指针到达字符右边界。

def func(string):
    length = len(string)

    left = 0
    right = 1

    result = ""

    while right < length:

        if string[left:right] in string[left+1:]:
            window_size = right - left
            if window_size > len(result):
                result = string[left:right]

            right += 1
            continue
        else:
            left += 1
            if left >= right:
                right += 1
                
    return result