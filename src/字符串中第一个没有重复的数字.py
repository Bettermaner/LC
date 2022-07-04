def first_word(string):
    map = {}

    for w in string:
        if w in map:
            map[w] = map[w] + 1
        else:
            map[w] = 1

    for index,w in enumerate(string):
        if map[w] == 1:
            return index, w