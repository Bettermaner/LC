
# 解题思路，回溯

def letterCombinations(self, dig_array: str) -> List[str]:

        def dfs(result,phoneMap,dig_array,index,combintion):

            # 当回溯的长度达到array的长度，则加入到result中
            if index == len(dig_array):
                result.append("".join(combintion))
            else:
                strings = phoneMap[dig_array[index]]
                for s in strings:
                    combintion.append(s)
                    dfs(result,phoneMap,dig_array,index+1,combintion)
                    # 立即还原位置
                    combintion.pop()

        phoneMap = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
        }
        result = []
        combintion = []
        if not dig_array:
            return result
            
        dfs(result,phoneMap,dig_array,0,combintion)


        return result





print(func(["2","3","5"]))