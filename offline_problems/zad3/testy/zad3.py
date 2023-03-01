# Jan Augustyn
# Algorytm opiera się na sortowaniu Bucket Sort.
# 1) Funkcja bucket_sort() rozdziela elementy do n//7 + 1 "kubełków". B[i] - i-ty "kubełek".
# 2) Jeżeli w B[i] jest więcej niż 100 elementów, to B[i] sortowane jest przez sortowanie kubełkowe,
# w przeciwny wypadku sortowany jest algorytmem Insertion Sort.
# 3) Przepisanie elementów z kubełków do tablicy wynikowej.
# Złożoność czasowa O(n^2)
# Złożoność pamięciowa O(n)

from zad3testy import runtests


def insertion_sort(A):
    for i in range(1, len(A)):
        curr = A[i]
        j = i - 1
        while j >= 0 and A[j] > curr:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = curr
# end


def interval_bucket_sort(T, b_beg, b_range):
    n = len(T)
    b_size = b_range / n
    b_num = int(b_range // b_size) + 1

    B = [[] for _ in range(b_num)]

    for i in range(n):
        B[int((T[i] - b_beg) // b_size)].append(T[i])

    for i in range(b_num):
        insertion_sort(B[i])

    k = 0
    for i in range(b_num):
        for j in range(len(B[i])):
            T[k] = B[i][j]
            k += 1
# end


def bucket_sort(T, n):
    B = []
    b_size = 7
    b_num = int((n/b_size)//1) + 1
    for i in range(b_num):
        B.append([])

    for j in T:
        B[int(j // b_size)].append(j)

    for i in range(b_num):
        if len(B[i]) <= 100:
            insertion_sort(B[i])
        else:
            interval_bucket_sort(B[i], i*b_size, b_size)

    k = 0
    for i in range(b_num):
        curr_bn = len(B[i])
        T[k:k+curr_bn] = B[i][:]
        k += curr_bn
    return T
# end


def SortTab(T, P):
    return bucket_sort(T, len(T))
# end


runtests( SortTab )
