def lms(array):
    n = len(array)
    lens_of_subs = [1] * n
    for i in range(len(array)):
        lens_of_subs[i] = 1

        for j in range(i):
            if array[i] % array[j] == 0 and lens_of_subs[j] + 1 > lens_of_subs[i]:
                lens_of_subs[i] = lens_of_subs[j] + 1
    return lens_of_subs


n = int(input())
arr = list(map(int, input().split()))

print(max(lms(arr)))
