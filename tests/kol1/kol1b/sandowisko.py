def str_counting_sort(k, N, n, arr):
    C = [0 for _ in range(N)]

    for a in arr:
        C[a[0][k]] += 1

    for i in range(N-1, 0, -1):
        C[i - 1] += C[i]

    B = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        j = arr[i][0][k]
        C[j] -= 1
        B[C[j]] = arr[i]

    arr[:] = B[:]
# end

 #      "ac"                  "ab"                "ad"               "bc"


T = [[[1, 1, 0, 0], 3], [[1, 1, 0, 0], 2], [[1, 0, 0, 1], 2], [[0, 1, 1, 0], 2]]
print(T)
for i in range(3, -1, -1):
    str_counting_sort(i, 3, len(T), T)
    # print(T)
print(T)