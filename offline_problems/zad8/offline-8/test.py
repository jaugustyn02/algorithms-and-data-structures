def MST(M):
    n = len(M)
    E = [(M[p][q], p, q) for p in range(n) for q in range(p)]
    print(E)


M = [[0, 1, 2],
     [1, 0, 10],
     [2, 10, 0]]
MST(M)