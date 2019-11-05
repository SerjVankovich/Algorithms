from comparators import default_comparator


def selection_sort(array, comparator=default_comparator, reverse=False):
    sign = -1 if reverse else 1
    for i in range(len(array) - 1):
        minimum = i
        for j in range(i, len(array)):
            if sign * comparator(array[j], array[minimum]) < 0:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]


array = list(map(int, input().split()))
selection_sort(array, reverse=True)
print(array)
