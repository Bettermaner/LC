
# 解题思路，回溯

def func(dig_array):
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

    dfs(result,phoneMap,dig_array,0,combintion)


    return result


def dfs(result,phoneMap,dig_array,index,combintion):

    if index == len(dig_array):
        result.append(",".join(combintion))
    else:
        strings = phoneMap[dig_array[index]]
        for s in strings:
            combintion.append(s)
            dfs(result,phoneMap,dig_array,index+1,combintion)
            combintion.pop()


print(func(["2","3","5"]))