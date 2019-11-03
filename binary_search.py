# binary_search works only on sorted lists
def binary_search(array, elem):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (right + left) // 2
        if array[middle] == elem:
            return middle
        elif array[middle] > elem:
            right = middle - 1
        else:
            left = middle + 1
    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(array, 7))
print(binary_search(array, 5))
print(binary_search(array, 11))
