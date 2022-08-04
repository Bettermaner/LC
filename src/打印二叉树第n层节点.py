# 解题思路
    # 递归

def func(root , n):
    if not root:
        return 

    if n == 1:
        print(root.value)

    else:
        func(root.left,n-1)
        func(root.right,n-1)
        
func(root,2)
    