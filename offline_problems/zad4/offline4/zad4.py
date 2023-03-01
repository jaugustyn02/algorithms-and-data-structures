# Jan Augustyn
# T[i] = [wysokość, początek, koniec, koszt] {i-tego akademiku}
# Algorytm składa się z 3 części:
# 1) Utworzenia tablicy indeksów (w celu zachowania początkowej kolejności), a następnie posortowania jej rosnąco względem końców budynków.
# 2) Utworzenia tablicy F o wymiarach (N+1) * (p+1), a następnie wypełnieniu jej analogicznie jak w dys. prob. plecakowym, tzn.:
# F[i][j] = (łączna liczba studentów z wybranych budynków, koniec najdalej kończoncego się budynku) {i-ty wiersz - budynek, j-ta kolumna - budżet}
# Gdy koszt i-tego bud. przekracza budżet:(*) F[i][j] = F[i-1][j], wpw. najpierw znajdowana jest (poprzez wyszukiwanie binarne) maks. liczba stud. (x)
# w (j-koszt)-kolumnie od 0 do i-1 wiersza, dla której koniec najdalszego budynku jest mniejszy niż początek i-tego budynku.
# Następnie, gdy F[i-1][j][0] >= (x + liczba stud. w i-tym bud.) to (*), wpw. F[i][j] = (liczba stud. w i-tym bud. + x, koniec i-tego bud.)
# 3) Odtworzeniu rozwiązania, poprzez liniowe przejście po tablicy F, zaczynając od elementu F[n][p], dodając kolejne budynki do tablicy result.
# n - liczba budynków
# p - całkowity budżet
# Złożoność czasowa O(nlog(n)*p)
# Złożoność pamięciowa O(np)

from zad4testy import runtests


def select_buildings(T, p):

    def bin_search_val(l, r, val, j):
        nonlocal F
        while l < r:
            mid = (l + r) // 2
            if val < F[mid][j][1]:
                r = mid
            else:
                l = mid + 1
        if F[r][j][1] > val and r > 0:
            return F[r-1][j][0]
        return F[r][j][0]
    # end

    def custom_key(i):
        nonlocal T
        return T[i][2]
    # end

    n = len(T)
    indices = [i for i in range(n)]
    indices.sort(key=custom_key)

    F = [[(0, 0) for _ in range(p+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        h, a, b, w = T[indices[i-1]]
        for j in range(1, p+1):
            if w > j:
                F[i][j] = F[i-1][j]
            else:
                max_poss_val = bin_search_val(0, i-1, a-1, j-w)
                total_value = h * (b - a) + max_poss_val
                if F[i-1][j][0] >= total_value:
                    F[i][j] = F[i-1][j]
                else:
                    F[i][j] = (total_value, b)

    result = []
    i = n
    j = p
    max_value = F[i][j][0]
    while max_value > 0:
        while i > 0 and F[i][j] == F[i-1][j]:
            i -= 1
        result.append(indices[i-1])
        h, a, b, w = T[indices[i - 1]]
        max_value -= h * (b - a)
        j -= w
        i -= 1
        while i > 0 and a <= F[i][j][1]:
            i -= 1

    return result
# end


runtests( select_buildings )
