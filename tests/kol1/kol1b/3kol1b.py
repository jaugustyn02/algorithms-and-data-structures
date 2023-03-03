# Jan Augustyn

from kol1btesty import runtests


def radix_sort(max_len, arr):
    n = len(arr)
    if n < 2: return arr
    word_n = len(arr[0][0])
    for i in range(word_n-1, -1, -1):
        str_counting_sort(i, max_len+1, n, arr)
# end


def str_counting_sort(k, N, n, arr):
    C = [0 for _ in range(N)]

    for a in arr:
        C[a[0][k]] += 1

    for i in range(N-1, 0, -1):
        C[i-1] += C[i]

    B = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        j = arr[i][0][k]
        C[j] -= 1
        B[C[j]] = arr[i]

    arr[:] = B[:]
# end


def len_count_x_bucket_sort(N, n, arr):
    C = [0 for _ in range(N)]

    for i in range(n):
        C[arr[i][1]] += 1

    for i in range(N-1):
        C[i+1] += C[i]

    B = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        j = arr[i][1]
        C[j] -= 1
        B[C[j]] = arr[i]

    A = []
    i = -1
    curr_len = 0
    for a in B:
        if a[1] > curr_len:
            i += 1
            curr_len = a[1]
            A.append([])
            A[i].append(a)
        else:
            A[i].append(a)

    return A
# end


def chars_count(a):
    n = len(a)
    first = ord('a')
    last = ord('z')
    N = last-first + 1
    C = [0 for _ in range(N)]

    for c in a:
        C[ord(c)-first] += 1

    return C, n
# end


def f(T):
    n = len(T)
    max_len = 0
    for i in range(n):
        T[i] = chars_count(T[i])
        max_len = max(max_len, T[i][1])

    T = len_count_x_bucket_sort(max_len+1, n, T)

    for i in range(len(T)):
        radix_sort(max_len, T[i])

    max_sub = 0
    for bucket in T:
        curr_sub = 1
        for i in range(len(bucket)-1):
            if bucket[i][0] == bucket[i+1][0]:
                curr_sub += 1
            else:
                max_sub = max(max_sub, curr_sub)
                curr_sub = 1
        max_sub = max(max_sub, curr_sub)

    return max_sub
# end


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
