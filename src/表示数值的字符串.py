class solution():
    "判断是一个字符串是否是数值"

    # 例如，字符串["+100","5e2","-123","3.1416","-1E-16"]都表示数值。
    # 但是["12e","1a3.14","1.2.3","+-5","12e+4.3"]都不是数值。
    # 一个 'e' 或 'E' ，前面是一个整数或者小数，后面跟着一个整数(可正可负)
    # 一个整数前面可以有 '+',或 '-'
    # 小数点前面后面可以有整数也可以无整数

    def __init__(self):
        self.index = 0


    def integer(self,string):
        if self.index < len(string) and (string[self.index] == "+" or string[self.index] == "-"):
            self.index += 1
        return self.unsigned_integer(string)

    def unsigned_integer(self,string):
        tmp_index = self.index
        while self.index < len(string) and (string[self.index] >= "0" and string[self.index] <= "9"):
            self.index += 1
        return self.index > tmp_index

    def is_number(self,string):
        # 解题思路：遍历

        l = len(string)
        # 先去除掉字符串左右两边的空格

        for i in range(l):
            if self.index < l  and string[self.index] == " ":
                self.index += 1

        end = l - 1
        while end > 0 and (string[end] == " "):
            end -= 1
        #向右一格    
        end += 1
        
        # 表示该字符串为空串
        if self.index > end:
            return False

        # 判断是否有整数部分
        flag = self.integer(string)

        # 判断是否有小数部分
        if self.index <= end and string[self.index] == ".":
            self.index += 1
            #小数点前后有无数字可选
            flag = self.unsigned_integer(string) or flag

        # 判断是否有e
        if self.index <= end and (string[self.index] == "e" or string[self.index] == "E") :
            self.index +=1
            #e后面必须全是整数
            flag = self.integer(string) and flag

        #是否字符串遍历结束
        return flag and self.index == end


