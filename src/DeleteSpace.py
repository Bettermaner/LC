def delete_space(string):
    "请实现一个函数,将一个字符串s中的每个空格替换成“%20”"

    if not string:
        return string

    delete_space_string = ""

    for i in string:
        if i == " ":
            delete_space_string += "%20"
        else:
            delete_space_string += i
    return delete_space_string
