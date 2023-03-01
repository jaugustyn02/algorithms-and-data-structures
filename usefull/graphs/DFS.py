from Graph import UndirectedGraph


def dfs(v, vis, adj_ls):
    for u in adj_ls[v]:
        if not vis[u]:
            vis[u] = 1
            dfs(u, vis, adj_ls)
            # print("wierzochłek {} przetworzony".format(u))
# end def


def dfs_time(v, vis, adj_ls, time, curr_time=0):
    for u in adj_ls[v]:
        if not vis[u]:
            vis[u] = 1
            curr_time = dfs_time(u, vis, adj_ls, time, curr_time)
            time[u] = curr_time
            curr_time += 1
            print("wierzochłek {} przetworzony".format(u))
    return curr_time
# end def


def main():
    V = 7
    s = 0
    graph = UndirectedGraph(ver=V, den=2)
    graph.print()
    visited = [0 for _ in range(V)]
    visited[s] = 1
    dfs(s, visited, graph.adjacency_list)

    visited = [0 for _ in range(V)]
    proc_time = [-1 for _ in range(V)]
    visited[s] = 1
    proc_time[s] = dfs_time(s, visited, graph.adjacency_list, proc_time)
    print(proc_time)
# end main



if __name__ == "__main__":
    main()
# end if
