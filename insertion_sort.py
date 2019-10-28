from comparators import default_comparator


def insertion_sort(array, comparator=default_comparator, reverse=False):
    sign = -1 if reverse else 1
    for i in range(1, len(array)):
        j = i
        while j > 0 and sign * comparator(array[j], array[j - 1]) < 0:
            tmp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = tmp
            j -= 1
    return array


array = list(map(int, input().split()))
insertion_sort(array)

print(array)
