def re_macth(string,pattern):
    "正则表达式匹配"
    # 解题思路： 动态规划
    # 1.模式中的字符'.'表示任意一个字符
    # 2.模式中的字符'*'表示它前面的字符可以出现任意次（包含0次）。
    # 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
    if string == None or pattern == None:
        return False

    # 确定状态转移方程
    # (指当前pattern长度为j时的最后一位字符) pattern[j-1]为'*' 
        # 如果str[i-1]== pattern[j-2 ]或者pattern[j-2] == '.'，那么pattern数组中'*'前面字符可以出现任意次，
        # 则其状态转移方程为$dp[i][j] = dp[i][j - 2] || dp[i - 1][j]$;
        # 否则模式的'*'前一位字符与字符串的上个字符不匹配，那么状态转移方程为$dp[i][j]=dp[i-][j-2]$
    # 如果(当前pattern长度为j时的最后一位字符与字符串长度为i时的最后一位的字符匹配)，
        # 即str[i-1]== pattern[j-1 ]或者pattern[j-1] == '.'，状态转移方程$dp[i][j]=dp[i-1][j-1]$

    n = len(string)
    m = len(pattern)

    # 将0长度字符串与0长度pattern的情况加入dp中
    # n表示当字符串长度为n的情况
    # m表示pattern长度为m的情况
    dp = [[ False for j in range(m + 1)] for i in range(n + 1)]
    dp[0][0] = True

    for i in range(n + 1):
        # 当j为0时表示pattern长度为0,除了string长度也为0外,其他情况必定为False,所以目前从parttern长度为1开始遍历
        for j in range(1,m+1):

            if j > 1 and pattern[j -1] == "*":
                # 如果当前pattern长度为j时的倒数第二个字符与字符串长度为i时的最后一位的字符匹配
                if i > 0 and (pattern[j-2] == string[i-1] or pattern[j-2] == "."):
                    # 两种情况,第一种是接受*,然后继续移动string，第二种不接受*,把pattern的倒数两位字符跳过,当做没存在过,重新比较string
                    dp[i][j] = dp[i-1][j] or dp[i][j-2]
                else:
                    # 如果当前pattern长度为j时的倒数第二个字符与字符串长度为i时的最后一位的字符不匹配,直接把pattern的倒数两位字符跳过,当做没存在过,重新比较string
                    # 还包含string长度为0的情况, 如 "" match "a*" => True
                    dp[i][j] = dp[i][j-2]
            
            elif i > 0  and (pattern[j-1] == "." or string[i-1] ==pattern[j-1]):
                dp[i][j] = dp[i-1][j-1]

    return dp[n][m]
                
