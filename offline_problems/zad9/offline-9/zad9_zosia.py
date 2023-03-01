from zad9testy import runtests
from math import inf
from copy import deepcopy
from collections import deque


def przeplywy(tab,s,t,num_verdex):
    def bfs(s, num_verdex, t, tab, parent):
        visited = [False for _ in range(num_verdex)]
        q = deque()
        q.append(s)
        visited[s] = True
        while len(q) > 0:
            u = q.popleft()
            for i in range(len(tab[u])):
                if not visited[i] and tab[u][i] != 0:
                    visited[i] = True
                    parent[i] = u
                    q.append(i)
            if visited[t]: return True
        return False

    maksy_flow=0
    parent = [None for _ in range(num_verdex)]

    while bfs(s,num_verdex,t, tab, parent):
        v=t
        flow=inf
        while v!=s:
            flow=min(flow,tab[parent[v]][v])
            v=parent[v]
        maksy_flow+=flow
        v=t
        while v!=s:
            tab[parent[v]][v]-=flow
            tab[v][parent[v]]+=flow
            v=parent[v]

    return maksy_flow


def maxflow( G,s ):
    result = 0
    num_verdex = 0
    for e in G:
        if e[0] > num_verdex:
            num_verdex = e[0]
        elif e[1] > num_verdex:
            num_verdex = e[1]
    num_verdex += 1
    tab = [[0 for _ in range(num_verdex)] for _ in range(num_verdex)]
    max_flow_solo = [0 for _ in range(num_verdex)]
    max_flow_pair = [[0, i, j] for i in range(num_verdex-1) for j in range(i+1, num_verdex)]

    for e in G:
        tab[e[0]][e[1]] = e[2]
        max_flow_solo[e[1]] += e[2]
    tab_copy = deepcopy(tab)

    for pair in max_flow_pair:
        if pair[1] != s and pair[2] != s:
            pair[0] = max_flow_solo[pair[1]] + max_flow_solo[pair[2]]

    max_flow_pair.sort(reverse=True)

    for pair in max_flow_pair:
        if pair[0] <= result: break
        i, j = pair[1], pair[2]
        tab_copy[i][j] = inf
        flow = przeplywy(tab_copy, s, j, num_verdex)
        result = max(result, flow)
        for i in range(num_verdex):
            tab_copy[i][:] = tab[i][:]

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )