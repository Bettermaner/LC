def longest_palindrome(string):
    "最长回文子串"

    string_len = len(string)
    if string_len <= 1:
        return string

    # 最长回文子串的起始下标
    start = 0
    # 最长回文子串长度，由于长度为1时必定为回文子串，所以长度默认为1
    max_length = 1
    # 建立二维表，dp[i][j],i表示当前起始的索引，j表示当前结尾的下标，dp[i][j]表示当前范围内的字符串是否为回文子串。
    dp = [[False for i in range(string_len)] for j in range(string_len)]

    # 在当前j个字符的情况下进行遍历,说明结尾下标目前为j
    for j in range(string_len):

        # i表示当前起始下标为i,最多能移动到j下标，结束
        for i in range(j+1):

            # 当起始下标与结尾下标一样或者相邻，比较两者下标对应的字符是否相等，相等则为子回文串
            if j - i < 2:
                dp[i][j] = string[i] == string[j]

            # 如果起始下标与结尾下标相差大于2了
            # 首先需要比较两者下标对应的字符是否相等，如果不相等则不是回文子串
            # 如果相等，则需要查看当前起始与结尾下标里面的部分是否是一个回文子串
            # 如果是，则当前是回文子串
            else:
                if string[i] == string[j] and dp[i+1][j-1]:
                    dp[i][j] = True

            if dp[i][j] and max_length < (j - i + 1):
                max_length = j - i + 1
                start = i

    return string[start:start+max_length], max_length


if __name__ == "__main__":

    print(longest_palindrome('asabbcbbagsgab'))
