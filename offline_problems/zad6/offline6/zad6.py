# Jan Augustyn
# Rozwiązanie składa się z 4 części:
# 1) Liniowym przejściu po grafie używając algorytmu bfs, do znalezienia wszystkich możliwych
#    najkrótszych ścieżek z wierz. s do wierz. t (również sprawdzeniu, czy taka ścieżka w ogóle istnieje).
# 2) Liniowym przejściu po grafie, począwszy od wierz. t, w celu znalezienia i zapisania
#    wszystkich wierzchołków, które zawierają się w najkrótszych ścieżkach.
# 3) Na zliczeniu wszystkich możliwych najkrótszych ścieżek względem odległośći od wierz. s
# 4) Sprawdzeniu, czy istnieje taka krawędź, którą zawierają wszystkie najkrótsze ścieżki.
# V - liczba wierzchołków
# G - liczba krawędzi
# Złożoność czasowa: O(V+G)
# Złożoność pamięciowa: O(V)

from zad6testy import runtests
from collections import deque


def bfs(s, t, G, V, P, D):
    for i in range(V):
        D[i] = V+1
        P[i] = -1

    visited = [0 for i in range(V)]
    visited[s] = 1
    D[s] = 0
    queue = deque([s])
    while len(queue) > 0:
        ver = queue[0]
        queue.popleft()
        for i in range(len(G[ver])):
            if not visited[G[ver][i]]:
                visited[G[ver][i]] = 1
                D[G[ver][i]] = D[ver] + 1
                P[G[ver][i]] = ver
                queue.append(G[ver][i])
                if G[ver][i] == t:
                    return True
    return False
# end


def copy_vertices(MPD, t, D, G):
    queue = deque([t])
    MPD[t] = D[t]
    while len(queue) > 0:
        ver = queue[0]
        queue.popleft()
        target_dist = D[ver]-1
        for ver in G[ver]:
            if D[ver] == target_dist:
                MPD[ver] = D[ver]
                queue.append(ver)
# end


def longer( G, s, t ):
    V = len(G)
    predecessors = [0 for i in range(V)]
    distances = [0 for i in range(V)]

    if not bfs(s, t, G, V, predecessors, distances):
        return None

    min_path = distances[t]
    min_path_distances = [0 for _ in range(V)]

    copy_vertices(min_path_distances, t, distances, G)

    paths_counts = [0 for _ in range(min_path+1)]
    for dist in min_path_distances:
        paths_counts[dist] += 1

    paths_counts[s] = 1
    ver = t
    curr_dist = min_path
    while curr_dist > 0 and (paths_counts[curr_dist] != 1 or paths_counts[curr_dist-1] != 1):
        ver = predecessors[ver]
        curr_dist -= 1

    if curr_dist == 0:
        return None
    return predecessors[ver], ver
# end


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
