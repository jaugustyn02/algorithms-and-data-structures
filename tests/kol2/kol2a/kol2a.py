# Jan Augustyn
# Algorytm to 4 części:
# 1) Posortowanie tablicy indeksów względem położenia przystanków
# 2) Stworzeniu nowej tablicy tylko przystanków przesiadkowych i dodaniu im wartości (liczby przystanków kontrolnych między i-tym a i-1-tym przystanku)
# 3) Liniowym przejściu i wypełnieniu tablicy M i J czyli minimalnej liczbie przystanków gdy przyjeżdza Marcin i przyjeżdża Jacek
# 4) Odtworzeniu rozwiązania
# Złożoność czasowa: O(nlogn)
# Złożność pamięciowa: O(n)


from kol2atesty import runtests

def drivers( P, B ):
    def custom_key(i):
        nonlocal P
        return P[i][0]
    n = len(P)
    indices = [i for i in range(n)]
    indices.sort(key=custom_key)
    PP = []
    count = 0
    for i in range(n):
        if P[indices[i]][1]:
            PP.append([indices[i], count])
            count = 0
        else:
            count += 1
    pp_n = len(PP)
    J = [0 for _ in range(pp_n)]
    M = [0 for _ in range(pp_n)]
    M[0] = n+1
    M[1] = PP[1][1]
    M[2] = PP[2][1]
    for i in range(3, pp_n):
        J[i] = min(M[i-3:i])
        M[i] = min(J[i-1] + PP[i][1], J[i-2] + sum(PP[i-1:i+1][1]), J[i-3] + sum(PP[i-2:i+1][1]))
    # print(J)
    # print(M)
    if J[pp_n-1] < M[pp_n-1]:
        who = 0
    else: who = 1
    i = pp_n-1
    curr_count = min(J[pp_n - 1], M[pp_n - 1])
    result = []
    while i >= 0:
        if who == 0:
            while i >= 0 and M[i] != curr_count:
                i -= 1
            if i >= 0:
                result.append(PP[i][0])
        if i >= 0:
            curr_count -= PP[i][1]
            i -= 1
            if i >= 0:
                result.append(PP[i][0])

    return list((reversed(result)))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )