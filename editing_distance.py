def editing_distance(str1, str2):
    n = len(str1)
    m = len(str2)

    matrix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        matrix[i][0] = i
    for j in range(m + 1):
        matrix[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = matrix[i][j - 1] + 1
            removing = matrix[i - 1][j] + 1
            changing = matrix[i - 1][j - 1] + diff(str1[i - 1], str2[j - 1])
            matrix[i][j] = min(insertion, removing, changing)
    return matrix[n][m]


def diff(char1, char2):
    if char1 == char2:
        return 0
    else:
        return 1


def editing_distance_low_memory(str1, str2):
    n = len(str1)
    m = len(str2)

    current = list(range(m+1))

    for i in range(1, n + 1):
        previous = current
        current = [0] * (m+1)
        current[0] = i
        for j in range(1, m + 1):
            insertion = current[j - 1] + 1
            removing = previous[j] + 1
            changing = previous[j - 1] + diff(str1[i - 1], str2[j - 1])
            current[j] = min(insertion, removing, changing)
    return current[m]


first, second = input(), input()
print(editing_distance_low_memory(first, second))
print(editing_distance(first, second))
