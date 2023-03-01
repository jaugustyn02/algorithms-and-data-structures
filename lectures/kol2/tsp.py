def d(i, j, arr):
    x1, y1 = arr[i]
    x2, y2 = arr[j]
    a = x2 - x1
    b = y2 - y1
    return (a**2 + b**2)**0.5
# end


def tspf(S, t, arr):
    if len(S) == 0: return d(t, 0, arr)
    r = S.pop()
    min_path = tspf(S, r, arr) + d(r, t, arr)
    for i in range(len(S)-1, -1, -1):
        S[i], r = r, S[i]
        min_path = min(min_path, tspf(S, r, arr) + d(r, t, arr))
    S.append(r)
    return min_path
# end


def tsp_sol(arr):
    if len(arr) < 2: return 0
    C = [i for i in range(1, len(arr))]
    r = C.pop()
    min_path = tspf(C, r, arr) + d(r, 0, arr)
    print(min_path, r, C)
    # for i in range(len(C)-1, -1, -1):
    #     C[i], r = r, C[i]
    #     min_path = min(min_path, tspf(C, r, arr) + d(r, 0, arr))
    #     print(min_path, r, C)
    return min_path
# end


C = [(1, 2), (5, 2), (6, 8), (2, 2), (13, 5), (6, 9)]

print(tsp_sol(C))
