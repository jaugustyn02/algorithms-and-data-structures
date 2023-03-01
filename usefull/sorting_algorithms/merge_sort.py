from random_list import create_random_list
import time


def merge(l, m, r, tab):
    il = 0
    ir = 0
    left_tab = tab[l:m+1]
    right_tab = tab[m+1:r+1]
    nl = m-l+1
    nr = r-m
    for i in range(l, r+1):
        if ir >= nr or il < nl and left_tab[il] < right_tab[ir]:
            tab[i] = left_tab[il]
            il += 1
        else:
            tab[i] = right_tab[ir]
            ir += 1
# end


def merge_sort_list(l, r, tab):
    if l != r:
        m = (l+r)//2
        merge_sort_list(l, m, tab)
        merge_sort_list(m+1, r, tab)
        merge(l, m, r, tab)
# end


n = 1000000
a = 1
b = 10**24
new_ls = create_random_list(n, a, b)
# print(new_ls)
begin = time.time()

merge_sort_list(0, n-1, new_ls)

end = time.time()
print("czas:", round(end-begin, 2))

# print(new_ls)
