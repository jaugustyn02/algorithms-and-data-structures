# Jan Augustyn
# Algorytm składa się z 3 części
# 1) posortowanie każdego słowa względem znaków counting sortem
# 2) posortowanie słów między sobą, najpierw względem wartości, następnie względem alfabetu
# 3) przejście liniowe i znalezienie najdłuższego podciągu
# Złożoność czasowa O(NLogN) przy założeniu że quick sort sortuje w czasie nlon
# Złożoność pamięcia O(N)



from kol1btesty import runtests


def str_qs(p, r, arr):
    while p < r:
        q = partition(p, r, arr)
        if q - p < r - q:
            str_qs(p, q-1, arr)
            p = q + 1
        else:
            str_qs(q+1, r, arr)
            r = q - 1
# end


def partition(p, r, arr):
    pivo = arr[r]
    i = p - 1
    for j in range(p, r):
        if cmp(arr[j], pivo):
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i+1
# end


def cmp(a, b):
    if a[1] == b[1]:
        return a[0] < b[0]
    return a[1] < b[1]
# end


def str_count_sort(a):
    n = len(a)
    first = ord('a')
    last = ord('z')
    N = last-first + 1
    C = [0 for _ in range(N)]

    for c in a:
        C[ord(c)-first] += 1

    # for i in range(N-1):
    #     C[i+1] += C[i]

    # B = [0 for _ in range(n)]
    # for i in range(n-1, -1, -1):
    #     j = ord(a[i]) - first
    #     C[j] -= 1
    #     B[C[j]] = a[i]

    return C, n
# end


def f(T):
    n = len(T)
    max_len = 0
    for i in range(n):
        T[i] = str_count_sort(T[i])
        max_len = max(max_len, T[i][1])

    str_qs(0, n-1, T)

    max_sub = 0
    curr_sub = 1
    for i in range(n-1):
        if T[i][1] == T[i+1][1] and T[i][0] == T[i+1][0]:
            curr_sub += 1
        else:
            max_sub = max(max_sub, curr_sub)
            curr_sub = 1
    max_sub = max(max_sub, curr_sub)

    return max_sub
# end


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
