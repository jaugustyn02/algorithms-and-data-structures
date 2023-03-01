from zad2testy import runtests


def quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q - p > r - q:
            quicksort(A, q + 1, r)
            r = q - 1
        else:
            quicksort(A, p, q - 1)
            p = q + 1


def partition(tab, p, r):
    x = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j][0] < x[0] or (tab[j][0] == x[0] and tab[j][1] > x[1]):
            i += 1
            temp = tab[i]
            tab[i] = tab[j]
            tab[j] = temp
    temp = tab[i + 1]
    tab[i + 1] = tab[r]
    tab[r] = temp
    return i + 1


def depth(L):
    rozmiar = len(L)
    tab = L
    quicksort(tab, 0, rozmiar - 1)

    tab_pomoc = [True for _ in range(rozmiar)]
    maks = 0
    for i in range(rozmiar - 1):
        if tab_pomoc[i] is True:
            licznik = 0
            for j in range(i + 1, rozmiar):
                if tab[i][1] >= tab[j][1]:
                    tab_pomoc[j] = False
                    licznik += 1
            if licznik > maks:
                maks = licznik
    return maks


runtests( depth )