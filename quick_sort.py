from comparators import default_comparator


def quick_sort(array, comparator=default_comparator, reverse=False):
    if len(array) < 2:
        return array
    x = array[len(array) // 2]
    if reverse:
        return quick_sort(list(filter(lambda elem: -comparator(x, elem) > 0, array)), comparator, reverse) + \
               list(filter(lambda elem: comparator(x, elem) == 0, array)) + \
               quick_sort(list(filter(lambda elem: -comparator(x, elem) < 0, array)), comparator, reverse)
    else:
        return quick_sort(list(filter(lambda elem: comparator(x, elem) > 0, array)), comparator) + \
               list(filter(lambda elem: comparator(x, elem) == 0, array)) + \
               quick_sort(list(filter(lambda elem: comparator(x, elem) < 0, array)), comparator)


# Input array values like "2 7 9 4 3 5"
arr = list(map(int, input().split()))
sorted_array = quick_sort(arr)
print(sorted_array)
