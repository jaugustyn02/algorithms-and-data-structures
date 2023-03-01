# Jan Augustyn
# Algorytm opiera się na 3 częściach:
# 1) Wyliczeniu maksymalnej potęcjalnej łącznej ilości wpływającego paliwa do każdego wierzchołka (liczba ta może być
#    zawyżona względem faktycznego maksymalnego dopływu, jest to tylko oszacowanie).
# 2) Utworzeniu tablicy par wierzchołków (pomijając źródło), gdzie każdy element jest postaci:
#    [suma max potencjalnego dopływu obu wierz., 1 wierz, 2 wierz], a nast. posortowaniu jej malejąco względem dopływu.
# 3) Przejściu po tablicy par wierzchołków, sprawdzając algorytmem Edmondsa-Karpa maksymalny przepływ dla wierz. 2
#    będącego ujściem i połączenia wierz. 1 i 2 krawędzią o nieskończonej przepustowości. Główna pętla wykonuje się
#    dopóki wartość max potencjalnego dopływu dla aktualnie rozpatrywanej pary jest większa od aktualnego
#    maksymalnego znalezionego przepływu.
# Złożoność czasowa: O(V^3*E^2)
# Złożoność pamięciowa: O(V^2)

from zad9testy import runtests
from math import inf
from copy import deepcopy
from collections import deque


def augmenting_path_bfs(src, sink, V, pred, adj_mat):
    visited = [0 for _ in range(V)]
    queue = deque()
    queue.append(src)
    visited[src] = 1
    while len(queue) > 0:
        v = queue.popleft()
        for u in range(V):
            if not visited[u] and adj_mat[v][u] > 0:
                pred[u] = v, min(pred[v][1], adj_mat[v][u])
                visited[u] = 1
                queue.append(u)
        if visited[sink]: return True
    return False
# end def


def find_max_flow(source, sink, V, adj_mat):
    predecessors = [[-1, inf] for _ in range(V)]
    curr_flow = 0
    while augmenting_path_bfs(source, sink, V, predecessors, adj_mat):
        v = sink
        min_flow = predecessors[v][1]
        curr_flow += min_flow
        while v != source:
            adj_mat[predecessors[v][0]][v] -= min_flow
            adj_mat[v][predecessors[v][0]] += min_flow
            v = predecessors[v][0]
    return curr_flow
# end def


def potential_flow_dfs(v, s, V, adj_ls, mpf):
    if mpf[v] < 0:
        mpf[v] = 0
        if v == s: mpf[v] = inf
        for u, p in adj_ls[v]:
            if mpf[u] < 0:
                potential_flow_dfs(u, s, V, adj_ls, mpf)
            mpf[v] += min(p, mpf[u])
# end def


def maxflow( G, s ):
    V = max(max(e[0], e[1]) for e in G)+1
    adjacency_matrix = [[0 for _ in range(V)] for _ in range(V)]
    reversed_adjacency_list = [[] for _ in range(V)]
    for edge in G:
        adjacency_matrix[edge[0]][edge[1]] = edge[2]
        reversed_adjacency_list[edge[1]].append((edge[0], edge[2]))

    vertex_potential_flow = [-1 for _ in range(V)]
    for v in range(V):
        potential_flow_dfs(v, s, V, reversed_adjacency_list, vertex_potential_flow)

    pair_potential_flow = []
    for v in range(V-1):
        for u in range(v+1, V):
            if v != s and u != s:
                pair_potential_flow.append([vertex_potential_flow[v] + vertex_potential_flow[u], v, u])

    pair_potential_flow.sort(key=lambda x: x[0], reverse=True)

    max_flow = 0
    adj_matrix_cp = deepcopy(adjacency_matrix)
    for pair in pair_potential_flow:
        if pair[0] <= max_flow:
            return max_flow
        v, u = pair[1], pair[2]
        adj_matrix_cp[v][u] = inf
        max_flow = max(max_flow, find_max_flow(s, u, V, adj_matrix_cp))
        for v in range(V):
            adj_matrix_cp[v][:] = adjacency_matrix[v][:]
            # for u in range(V):
            #     adj_matrix_cp[v][u] = adjacency_matrix[v][u]

    return max_flow
# end def

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )