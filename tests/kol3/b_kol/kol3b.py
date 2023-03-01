# Jan Augustyn
# Algorytm składa się z 2 części:
# 1) Utworzeniu macierzy sąsiedztwa, gdzie każdy pole o indeksach u, v zawiera minimalny koszt dostania się
#    z wierzchołka u do v. Jeżeli istnieje droga z u do v, to obliczne jest min z kosztu paliwa i kosztu przelotu,
#    w przeciwnym razie jest to koszt przelotu.
# 2) Znalezieniu kosztu minimalnej ścieżki algorytmem Dijsktra.
# Złożoność czasowa: O(V^2logV)
# Złożoność pamięciowa: O(V^2)

from kol3btesty import runtests
from math import inf
from queue import PriorityQueue


def dijsktra(s, t, G):
    pq = PriorityQueue()
    dist = [inf for _ in G]
    dist[s] = 0
    pq.put((0, s))
    while not pq.empty():
        d, u = pq.get()
        if u == t: break
        for v, w in enumerate(G[u]):
            if dist[v] > d + w:
                dist[v] = d + w
                pq.put((d+w, v))
    return dist
# end def


def airports( G, A, s, t):
    V = len(G)
    adj_mat = [[A[u] + A[v] for v in range(V)] for u in range(V)]
    for u in range(V):
        for v, c in G[u]:
            adj_mat[u][v] = min(adj_mat[u][v], c)

    distance = dijsktra(s, t, adj_mat)
    return distance[t]
# end def


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )