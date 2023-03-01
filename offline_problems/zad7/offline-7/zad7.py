# Jan Augustyn
# Algorytm składa się z 3 części:
# 1) Sprawdzeniu spójności grafu, poprzez algorytm dfs
# 2) Sprawdzeniu, czy w grafie nie znajdują się liście
# 3.1) Utworzeniu macierzy sąsiedztwa względem 2 bram (możliwość sprawdzania istnienia scieżki w czasie stałym)
# 3.2) Przeszukiwaniu grafu w głąb, w celu znalezienia cyklu (różnica między algorytmem dfs, to ponowne ustawienie
#    wierzchołka jako nieodwiedzony, po rekurencyjnym sprawdzeniu wszystkich możliwych ścieżek wychodzących od niego)
# Złożoność czasowa: O(V!)
# Złożoność pamięciowa: O(V^2)

from zad7testy import runtests


def droga( G ):
    def dfs(v):
        nonlocal visited, G
        visited[v] = 1
        for u in G[v][0] + G[v][1]:
            if not visited[u]: dfs(u)
    # end

    def cycle_search(v, prev, n, last_gate):
        nonlocal result, visited, G, adjacency_matrix
        gate = 0
        if adjacency_matrix[v][0][prev]: gate = 1
        if n == len(G) and adjacency_matrix[v][gate][0] and adjacency_matrix[0][last_gate][v]:
            result[n-1] = v
            return 1
        visited[v] = 1
        for u in G[v][gate]:
            if not visited[u] and cycle_search(u, v, n + 1, last_gate):
                result[n-1] = v
                return 1
        visited[v] = 0
        return 0
    # end

    n = len(G)
    result = [-1 for _ in range(n)]
    adjacency_matrix = [[[0 for _ in range(n)] for _ in range(2)] for _ in range(n)]
    for v in range(n):
        for gate in range(2):
            for u in G[v][gate]:
                adjacency_matrix[v][gate][u] = 1

    visited = [0 for _ in range(n)]
    if n < 3: return None
    dfs(0)
    if 0 in visited: return None

    for i in range(n):
        for gate in range(2):
            if len(G[i][gate]) == 0:
                return None

    visited = [0 for _ in range(n)]
    cycle_search(0, G[0][1][0], 1, 1)
    if result[0] == -1: return None
    return result
# end


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )