# 解题思路
    # 递归
import copy

def func(root):
    result = []
    
    find_path(root,[],result)
    return result 

def find_path(root,tmp_path,result):
    if not root:
        return 

    tmp_path = copy.deepcopy(tmp_path)
    tmp_path.append(root)

    if not root.left and not root.right:
        result.append(tmp_path)
    else:
        find_path(root.left,tmp_path,result)
        find_path(root.right,tmp_path,result)