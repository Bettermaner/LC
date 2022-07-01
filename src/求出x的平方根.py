def my_sqrt(x):
    if x == 0:
        return 0

    i = 0
    while not (i * i < x and (i + 1) * (i + 1) > x):
        i += 1
        if i * i == x:
            break

    return i 