from zad2testy import runtests


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j][0] < pivot[0] or arr[j][0] == pivot[0] and arr[j][1] > pivot[1]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)


def depth(L):
    n = len(L)
    max_value = 0

    for x in L:
        if x[1] > max_value:
            max_value = x[1]

    if max_value <= 10 ** 7:
        quickSort(L, 0, n - 1)

        T = [0 for _ in range(max_value)]

        for x in L:
            T[x[1] - 1] += 1

        for i in range(max_value - 1):
            T[i + 1] += T[i]

        max_right = 0
        max_counter = 0
        for i in range(n - 1):
            r = L[i][1]
            if r > max_right:
                max_counter = max(max_counter, T[r - 1] - i - 1)
                max_right = r

        return max_counter
    else:
        return "lepiej nie sprawdzać :("


runtests(depth)
