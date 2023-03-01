from Graph import UndirectedGraph
from collections import deque
from math import inf


def bfs(s, adj_ls):
    visited = [0 for _ in range(len(adj_ls))]
    distance = [-1 for _ in range(len(adj_ls))]
    parent = [-1 for _ in range(len(adj_ls))]
    q = deque()
    q.append(s)
    visited[s] = 1
    distance[s] = 0
    while len(q) > 0:
        v = q.popleft()
        for u in adj_ls[v]:
            if not visited[u]:
                distance[u] = distance[v]+1
                visited[u] = 1
                parent[u] = v
                q.append(u)
    return visited, distance, parent
# end def


def main():
    V = 7
    graph = UndirectedGraph(ver=V, den=2)
    graph.print()
    v, d, p = bfs(0, graph.adjacency_list)
    print(v, d, p)
# end main


if __name__ == "__main__":
    main()
# end if
