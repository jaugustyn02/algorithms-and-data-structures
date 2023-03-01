from random_list import create_random_list
import time


def insertion_sort(p, r, T):
    for i in range(p+1, r+1):
        curr = T[i]
        while i > p and curr < T[i-1]:
            T[i] = T[i-1]
            i -= 1
        T[i] = curr
# end


def partition(p, r, T):
    q = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] < q:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1
# end


def quick_sort_list(p, r, T):
    while p < r:
        if r - p < 11:
            insertion_sort(p, r, T)
            return
        q = partition(p, r, T)
        if q - p < r - q:
            quick_sort_list(p, q - 1, T)
            p = q + 1
        else:
            quick_sort_list(q + 1, r, T)
            r = q - 1
# end



def insertion_sort_list(tab, n):
    for i in range(1, n):
        curr = tab[i]
        i -= 1
        while i > -1 and curr < tab[i]:
            tab[i+1] = tab[i]
            i -= 1
        tab[i+1] = curr
# end


n = 1000
a = 1
b = 10**6
sum_qs, sum_in = 0, 0
N = 100
for _ in range(N):
    new_ls = create_random_list(n, a, b)
    ls_copy = new_ls
# print(new_ls)
    begin = time.time()

    quick_sort_list(0, n-1, new_ls)

    end = time.time()
    sum_qs += end-begin
    # print("tim sort - czas:", round(end-begin, 5))


    begin = time.time()

    quick_sort_list(0, n-1, ls_copy)

    end = time.time()
    sum_in += end-begin
    # print("insertion sort - czas:", round(end-begin, 5))
    
print("tim sort - czas:", round(sum_qs/N, 5))
print("insertion sort - czas:", round(sum_in/N, 5))
