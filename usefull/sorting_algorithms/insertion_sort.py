from random_list import create_random_list


def insertion_sort_list(tab, n):
    for i in range(1, n):
        curr = tab[i]
        i -= 1
        while i > -1 and curr < tab[i]:
            tab[i+1] = tab[i]
            i -= 1
        tab[i+1] = curr
# end


n = 100
a = 1
b = 10**6
new_ls = create_random_list(n, a, b)
# print(new_ls)
insertion_sort_list(new_ls, n)
# print(new_ls)
