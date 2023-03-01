from gentests import runtests


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j][0] < pivot[0] or arr[j][0] == pivot[0] and arr[j][1] > pivot[1]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
# end


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
# end


def depth(L):

    n = len(L)
    quickSort(L, 0, n-1)

    tab = [1 for _ in range(n)]
    max_count = 0

    for i in range(n-1):
        if tab[i]:
            count = 0
            for j in range(i+1, n):
                if L[j][1] <= L[i][1]:
                    tab[j] = 0
                    count += 1
            max_count = max(max_count, count)

    return max_count
# end


runtests(depth)