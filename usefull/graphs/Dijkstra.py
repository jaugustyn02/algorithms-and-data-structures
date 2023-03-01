from Graph import UndirectedGraph
from queue import PriorityQueue
from math import inf


def dijsktra_sp(s, G):
    def relax(u, d, v, w):
        nonlocal pq, dist, prev
        if dist[v] > d + w:
            dist[v] = d + w
            prev[v] = u
            pq.put((d+w, v))

    pq = PriorityQueue()
    dist = [inf for _ in G]
    prev = [-1 for _ in G]
    prev[s] = s
    dist[s] = 0
    pq.put((0, s))
    while not pq.empty():
        d, u = pq.get()
        for v, w in G[u]:
            relax(u, d, v, w)
            # if dist[v] > d + w:
            #     dist[v] = d + w
            #     prev[v] = u
            #     pq.put((d+w, v))
    return dist, prev
# end def


def main():
    graph = UndirectedGraph(ver=7, den=2, wg=True)
    # g = [[(1, 10), (6, 3)],[(0, 10), (2, 6), (4, 4), (5, 10)],[(1, 6), (5, 9)],[(6, 6)],[(1, 4), (6, 10)],[(1, 10), (2, 9), (6, 6)],[(0, 3), (3, 6), (4, 10), (5, 6)]]
    graph.print()
    d, p = dijsktra_sp(0, graph.adjacency_list)
    print(d)
    print(p)
# end main


if __name__ == "__main__":
    main()
# end if

