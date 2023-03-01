from zad3testy import runtests


def floor(n):
    return int(n // 1)
# end


def insertion_sort(A):
    for i in range(1, len(A)):
        curr = A[i]
        j = i - 1
        while j >= 0 and A[j] > curr:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = curr
# end


def bucket_sort(T, bs):
    n = len(T)
    B = []
    bn = floor(n/bs) + 1

    for i in range(bn):
        B.append([])

    for j in T:
        B[int(j // bs)].append(j)

    for i in range(bn):
        # if len(B[i]) <= 100:
        insertion_sort(B[i])
        # else:
        #     # maybe tim sort?

    main_i = 0
    for i in range(bn):
        curr_bn = len(B[i])
        T[main_i:main_i+curr_bn] = B[i][:]
        main_i += curr_bn
    return T
# end


def SortTab(T, P):
    return bucket_sort(T, 7)
# end


runtests( SortTab )
