from comparators import default_comparator


def merge(a1, a2, comparator, sign):
    pointer1 = 0
    pointer2 = 0
    result = []
    for i in range(len(a1) + len(a2)):
        if pointer1 >= len(a1):
            result += a2[pointer2:]
            break
        if pointer2 >= len(a2):
            result += a1[pointer1:]
            break
        if sign * comparator(a1[pointer1], a2[pointer2]) > 0:
            result.append(a2[pointer2])
            pointer2 += 1
        else:
            result.append(a1[pointer1])
            pointer1 += 1
    return result


def merge_sort(array, comparator=default_comparator, reverse=False):
    sign = -1 if reverse else 1
    if len(array) <= 1:
        return array
    m = len(array) // 2
    return merge(merge_sort(array[:m], comparator, reverse), merge_sort(array[m:], comparator, reverse), comparator, sign)


array = list(map(int, input().split()))
sorted_array = merge_sort(array)

print(sorted_array)
