# Jan Augustyn
# Algorytm składa się z 2 części:
# 1) Sortowanie listy L (rosnąco po 1 wartości, malejąco po 2 wartości) - co gwarantuje, że każdy
# kolejny przedział w liście na pewno nie zawiera w sobie poprzedniego lub jest równy poprzedniemu.
# 2) Na przejściu po liście L i zliczaniu kolejnym przedziałom zawieranych przedziałów.
# Algorytm został zoptymalizowany w głównym stopniu poprzez zapamiętywanie i pomijanie przedziałów,
# które są zawierane, przez zastosowanie wyszukiwania binarnego do określania zasięgu przeszukiwania
# oraz przyśpieszenie algorytmu sortującego, np. używając alg. insertion sort dla małych przedziałów.
# Złożoność czasowa: O(n^2)
# Złożoność pamięciowa: O(n)

from zad2testy import runtests


def insertion_sort(p, r, T):
    for i in range(p+1, r+1):
        curr0, curr1 = T[i]
        while i > p and (curr0 < T[i-1][0] or (curr0 == T[i-1][0] and curr1 > T[i-1][1])):
            T[i] = T[i-1]
            i -= 1
        T[i] = curr0, curr1
# end


def partition(p, r, T):
    q0, q1 = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j][0] < q0 or T[j][0] == q0 and T[j][1] > q1:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1
# end


def quick_sort(p, r, T):
    while p < r:
        if r - p < 11:
            insertion_sort(p, r, T)
            return
        q = partition(p, r, T)
        if q - p < r - q:
            quick_sort(p, q - 1, T)
            p = q + 1
        else:
            quick_sort(q + 1, r, T)
            r = q - 1
# end


def depth(L):
    n = len(L)
    quick_sort(0, n - 1, L)

    I = [1 for _ in range(n)]
    max_count = 0
    max_range = n - 1
    i = 0
    lim = 0
    while i < max_range:
        if I[i]:
            end = L[i][1] + 1
            r = n
            while lim < r:
                m = (lim + r) // 2
                if end > L[m][0]:
                    lim = m + 1
                else:
                    r = m

            if lim - i - 1 > max_count:
                count = 0
                for j in range(i+1, lim):
                    if L[j][1] < end:
                        I[j] = 0
                        count += 1
                if count > max_count:
                    max_count = count
                    max_range = n - max_count
        i += 1

    return max_count
# end


runtests(depth)
