# Jan Augustyn
# Program składa się z 2 części:
# 1) Tworzenie i posortowanie rosnąco po wagach tablicy krawędzi, gdzie każdy element to (waga, nr_wierzchołka, nr_wierzchołka)
# 2) Przejście po tablicy krawędzi używając 2 iteratorów (i, j), i - indeks krawędzi o aktualnie najmniejszej wadze, j - odpowiednio największej.
#    Jeżeli z krawędzi z zakresu i-j da się utworzyć spójny graf (drzewo rozpinające), to porównywana jest różnica wag z aktualnym minimum.
#    Spójność sprawdzana jest poprzez algorytm dfs.
# Złożność czasowa O(V^4)
# Złożność pamięciowa O(V^2)

from zad8testy import runtests
from collections import deque


def c(i, j, A):
    x = ((A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2)**0.5
    return int(-x // 1 * -1)
# end


def dfs(v, adj_ls, visited):
    visited[v] = 1
    for u in adj_ls[v]:
        if not visited[u]: dfs(u, adj_ls, visited)
# end


def check_connectivity(adj_ls, V):
    visited = [0 for _ in range(V)]
    dfs(0, adj_ls, visited)
    return 0 not in visited
# end


def highway( A ):
    V = len(A)
    E = V*(V-1)//2
    edges = [0 for _ in range(E)]
    k = 0
    for i in range(V-1):
        for j in range(i+1, V):
            edges[k] = c(i, j, A), i, j
            k += 1
    edges.sort(key=lambda a: a[0])
    adj_ls = [deque() for _ in range(V)]
    for i in range(V-1):
        adj_ls[edges[i][1]].append(edges[i][2])
        adj_ls[edges[i][2]].append(edges[i][1])
    min_time = float('inf')
    i = 0
    j = V - 2
    while j < E:
        smaller_time = edges[j][0] - edges[i][0] < min_time
        connected = check_connectivity(adj_ls, V)
        if smaller_time and connected:
            min_time = edges[j][0] - edges[i][0]
        if not smaller_time or connected:
            adj_ls[edges[i][1]].popleft()
            adj_ls[edges[i][2]].popleft()
            i += 1
        if not connected or j - i + 2 < V:
            j += 1
            if j < E:
                adj_ls[edges[j][1]].append(edges[j][2])
                adj_ls[edges[j][2]].append(edges[j][1])
    return min_time
# end

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )