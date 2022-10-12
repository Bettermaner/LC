# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

# 返回所有可能的结果。答案可以按 任意顺序 返回。

# 输入：s = "()())()"
# 输出：["(())()","()()()"]

# 当遍历到「左括号」的时候：
# 「左括号」数量加 1。
# 当遍历到「右括号」的时候：
# 如果此时「左括号」的数量不为 0，因为「右括号」可以与之前遍历到的「左括号」匹配，此时「左括号」出现的次数 -1；
# 如果此时「左括号」的数量为 0，「右括号」数量加 1。
# 通过这样的计数规则，得到的「左括号」和「右括号」的数量就是各自最少应该删除的数量。

# 回溯
# 首先我们利用括号匹配的规则求出该字符串 s 中最少需要去掉的左括号的数目 和右括号的数目 ，
# 然后我们尝试在原字符串 s 中去掉 lremove 个左括号和 rremove 个右括号，
# 然后检测剩余的字符串是否合法匹配，如果合法匹配则我们则认为该字符串为可能的结果，我们利用回溯算法来尝试搜索所有可能的去除括号的方案。

# 在进行回溯时可以利用以下的剪枝技巧来增加搜索的效率：

# 我们从字符串中每去掉一个括号，则更新 lremove 或者 rremove，
# 当我们发现剩余未尝试的字符串的长度小于lremove+rremove 时，则停止本次搜索。

# 当 lremove 和 rremove 同时为 0 时，则我们检测当前的字符串是否合法匹配，如果合法匹配则我们将其记录下来。
# 由于记录的字符串可能存在重复，因此需要对重复的结果进行去重，去重的办法有如下两种：

# 利用哈希表对最终生成的字符串去重。
# 我们在每次进行搜索时，如果遇到连续相同的括号我们只需要搜索一次即可，比如当前遇到的字符串为 "(((())"，
# 去掉前四个左括号中的任意一个，生成的字符串是一样的，均为 "((())"，
# 因此我们在尝试搜索时，只需去掉一个左括号进行下一轮搜索，不需要将前四个左括号都尝试一遍。

class Solution:
    def removeInvalidParentheses(self, s: str) :
        res = []

        lremove , rremove = 0, 0
        for i in s:
            if i == "(":
                lremove += 1

            elif i == ")":
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

            
        def is_valid(string):
            cnt = 0

            for i in string:
                if i == "(":
                    cnt += 1

                elif i == ")":
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0


        def helper(s, start, lremove, rremove):

            if lremove == 0 and rremove == 0:
                if is_valid(s):
                    res.append(s)
                return 

            for  i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                # 如果剩余的字符无法满足去掉的数量要求，直接返回
                if lremove + rremove > len(s) - i:
                    break
                # 尝试去掉一个左括号
                if lremove > 0 and s[i] == '(':
                    helper(s[:i] + s[i + 1:], i, lremove - 1, rremove)
                # 尝试去掉一个右括号
                if rremove > 0 and s[i] == ')':
                    helper(s[:i] + s[i + 1:], i, lremove, rremove - 1)
                # 统计当前字符串中已有的括号数量

        helper(s, 0, lremove, rremove)

        return res

print(Solution().removeInvalidParentheses("()())()"))