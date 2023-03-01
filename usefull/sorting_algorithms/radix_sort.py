# radix sort, zał: ciągi znaków o równej dł.


def str_counting_sort(k, n, arr):
    n_chars = ord('z') - ord('a') + 1
    C = [0 for _ in range(n_chars)]
    for i in range(n):
        # print(arr[i][k])
        C[ord(arr[i][k]) - ord('a')] += 1

    for i in range(n_chars-1):
        C[i+1] += C[i]

    B = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        j = ord(arr[i][k]) - ord('a')
        C[j] -= 1
        B[C[j]] = arr[i]

    return B
# end


def radix_sort(arr):
    n = len(arr)
    if n < 1:
        return []

    str_len = len(arr[0])
    for i in range(str_len-1, -1, -1):
        arr = str_counting_sort(i, n, arr)

    return arr
# end


T = ["siema", "aaabb", "ziomm", "ccbba", "cccba", "ratat"]
print(T)
T = radix_sort(T)
print(T)