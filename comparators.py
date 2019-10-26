def default_comparator(a, b):
    return a - b


def string_comparator(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1
