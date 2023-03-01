from random_list import create_random_list
import time


def heapify_list(i, n, tab):
    l = 2*i + 1
    r = 2*i + 2
    max_ind = i
    if l < n and tab[l] > tab[max_ind]:
        max_ind = l
    if r < n and tab[r] > tab[max_ind]:
        max_ind = r
    if max_ind != i:
        tab[i], tab[max_ind] = tab[max_ind], tab[i]
        heapify_list(max_ind, n, tab)
# end


def build_heap_list(tab, n):
    for i in range((n-1)//2, -1, -1):
        heapify_list(i, n, tab)
# end


def heap_sort_list(tab, n):
    build_heap_list(tab, n)

    for i in range(n-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify_list(0, i, tab)

# end


n = 1000000
a = 1
b = 10**24
new_ls = create_random_list(n, a, b)
# print(new_ls)
begin = time.time()

heap_sort_list(new_ls, n)

end = time.time()
print("czas:", round(end-begin, 2))

# print(new_ls)
