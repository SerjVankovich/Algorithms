import bisect


def lns(array):
    n = len(array)
    lens_of_subs = [-1] * (n + 1)
    lens_of_subs[-1] = 10 ** 10
    parents = [-1] * n
    for i in range(0, n):
        id = bisect.bisect_left(lens_of_subs, array[i])
        if -1 < id < n + 1:
            if lens_of_subs[id] >= array[i] >= lens_of_subs[id-1]:
                parents[id-1] = lens_of_subs[id]
                lens_of_subs[id-1] = array[i]
    answer = []
    i = len(parents) - 2
    j = 0
    if len(parents) == 1:
        answer = [1]
    else:
        while parents[i] != -1:
            while array[j] != parents[i]:
                j += 1
            answer.append(j + 1)
            j += 1
            i -= 1
        while array[j] != lens_of_subs[i+1]:
            j += 1
        answer.append(j+1)

    return n - (i + 1), answer


n = int(input())
arr = list(map(int, input().split()))
los, answer = lns(arr)
print(los)
print(*answer)