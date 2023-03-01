from zad2testy import runtests


def partition(p, r, T):
    q = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] > q:
            i = i + 1
            T[i], T[j] = T[j], T[i]

    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quickSort(p, r, T):
    if p < r:
        q = partition(p, r, T)
        quickSort(p, q - 1, T)
        quickSort(q + 1, r, T)
# end


def depth(L):
    n = len(L)
    S = [L[i][1] - L[i][0] for i in range(n)]
    quickSort(0, n-1, S)
    if n < 100:
        print(S)

    # I = [1 for _ in range(n)]
    # max_count = 0
    # i = 0
    # max_range = n-1
    # while i < max_range:
    #     if I[i]:
    #         l, r = L[i]
    #         count = 0
    #         for j in range(i+1, n):
    #             if :
    #                 count += 1
    #                 I[j] = 0
    #         if count > max_count:
    #             max_count = count
    #             max_range = n - max_count - 1       #  0 - 199 0 (1, 100) - 100    101 - (99, 199) 199-99+1 = 101 => i < 99 = 200 - 100 - 1
    #     i += 1
    # return max_count


runtests(depth)
