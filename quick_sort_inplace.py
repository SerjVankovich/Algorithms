from random import randint
from comparators import default_comparator


def quick_sort_in_place(array, comparator=default_comparator, reverse=False):
    def partition(arr, left, right):
        sign = -1 if reverse else 1
        random_num = randint(left, right - 1)
        j = left

        # swap random element and first
        tmp = arr[left]
        arr[left] = arr[random_num]
        arr[random_num] = tmp

        for i in range(left + 1, right):
            if sign * comparator(arr[i], arr[left]) <= 0:
                tmp = arr[j + 1]
                arr[j + 1] = arr[i]
                arr[i] = tmp
                j += 1
        tmp = array[j]
        array[j] = array[left]
        array[left] = tmp

        return j

    def helper(a, l, r):
        if l >= r:
            return
        j = partition(a, l, r)
        helper(a, l, j)
        helper(a, j + 1, r)

    helper(array, 0, len(array))


array = list(map(int, input().split()))
quick_sort_in_place(array)
print(array)
