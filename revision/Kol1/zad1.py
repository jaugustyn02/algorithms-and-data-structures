# Treść: przegrupuj elementy tablicy T tak, by pod główną przekątną znajdowały się tylko el. mniejsze
# od tych na przekątnej, a nad nią elementy większe.
# Najprostsze  rozwiązanie: przerzucam el. do pomocnicznej tablicy 1-wymiarowej
# Używając algoyrtmu statystyki pozycyjnej, grupuje elementy na 5 grup [ () < min < () < max < ()]
# Zapisuje w odpowiedniej kolejności el z tablicy pomocniczej do wynikowej
# Złożoność czas. O(n^2)
# Złożoność pam. O(n^2) - powinno się dać to zrobić w miejscu


def partition(p, r, arr):
    pivo = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] < pivo:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i + 1
# end


def regroup(p, r, k, arr):
    if p == r: return
    q = partition(p, r, arr)
    if q == k: return
    if q > k:
        regroup(p, q - 1, k, arr)
    else:
        regroup(q + 1, r, k, arr)
# end


def Median(T):
    n = len(T)
    if n < 2: return T
    N = n*n
    mid = N//2
    half = n//2
    k1 = mid - half
    k2 = mid + half
    if n % 2 == 0:
        k2 -= 1

    T_help = [0 for _ in range(N)]

    k = 0
    for i in range(n):
        for j in range(n):
            T_help[k] = T[i][j]
            k += 1

    regroup(0, N-1, k1, T_help)
    regroup(k1+1, N-1, k2, T_help)

    up_ind = k2+1
    mid_ind = k1
    down_ind = 0
    for i in range(n):
        for j in range(n):
            if j < i:
                T[i][j] = T_help[down_ind]
                down_ind += 1
            elif i == j:
                T[i][j] = T_help[mid_ind]
                mid_ind += 1
            else:
                T[i][j] = T_help[up_ind]
                up_ind += 1
    return T
# end


T = [[2, 432, 22], [6, 23, 2], [767, 32, 12]]
# T = [ [ 2, 3, 5],
# [ 7,11,13],
# [17,19,23] ]

print(Median(T))
