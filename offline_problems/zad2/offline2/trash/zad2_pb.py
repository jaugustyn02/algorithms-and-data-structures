from zad2testy import runtests
# from time import time


def binary_search(x, l, r, T):
    while l < r:
        m = (l+r)//2
        if x > T[m][0]:
            l = m+1
        else:
            r = m
    return l


def partition(p, r, T):
    q0, q1 = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j][0] < q0 or T[j][0] == q0 and T[j][1] > q1:
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
    # begin = time()

    quickSort(0, n-1, L)

    # end = time()
    # print("posortowano w:", round(end-begin, 2))

    # begin = time()

    I = [1 for _ in range(n)]
    max_count = 0

    max_range = n - 1
    i = 0
    lim = 0
    while i < max_range:
        if I[i]:
            right = L[i][1]
            # lim = binary_search(right+1, lim+1, n, L)
            x = right + 1
            r = n
            while lim < r:
                m = (lim + r) // 2
                if x > L[m][0]:
                    lim = m + 1
                else:
                    r = m

            if lim - i - 1 > max_count:
                count = 0
                for j in range(i+1, lim):
                    if L[j][1] <= right:
                        I[j] = 0
                        count += 1
                if count > max_count:
                    max_count = count
                    max_range = n - max_count
        i += 1

    return max_count
# end


runtests(depth)
