from random_list import create_random_list


def bubble_sort_list(tab, n):
    chg = True
    while chg:
        chg = False
        for i in range(n-1):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = ta[i+1], tab[i]
                chg = True
# end


n = 10
a = 1
b = 10
new_ls = create_random_list(n, a, b)
print(new_ls)
bubble_sort_list(new_ls, n)
print(new_ls)