def prom(P, g, d):
    def f(i, d_curr, g_curr):  # zwraca max liczbę zmieszczonych samochodów
        nonlocal n, d, g, P, F
        if d_curr > d or g_curr > g:
            return -1
        if F[i][d_curr][g_curr] != -1:
            return F[i][d_curr][g_curr]
        if i == n or (d_curr == d and g_curr == g):
            F[i][d_curr][g_curr] = 0
            return 0
        if d_curr == d:
            tmp = f(i + 1, d_curr, g_curr + P[i]) + 1
        elif g_curr == g:
            tmp = f(i + 1, d_curr + P[i], g_curr) + 1
        else:
            tmp = max(f(i + 1, d_curr + P[i], g_curr), f(i + 1, d_curr, g_curr + P[i])) + 1
        F[i][d_curr][g_curr] = tmp
        return tmp

    count = 0
    n = len(P)
    F = [[[-1 for _ in range(g+1)] for _ in range(d+1)] for _ in range(n+1)]
    noc = f(0, 0, 0)
    # print(F[1][P[0]][0], F[1][0][P[0]])
    d_result = []
    g_result = []
    d_curr = 0
    g_curr = 0
    noc_curr = noc - 1
    for i in range(noc):
        if P[i] + d_curr < d+1 and F[i+1][P[i] + d_curr][g_curr] == noc_curr:
            d_result.append(i)
            d_curr += P[i]
        elif P[i] + g_curr < g+1 and F[i+1][d_curr][P[i] + g_curr] == noc_curr:
            g_result.append(i)
            g_curr += P[i]
        noc_curr -= 1

    if d_result[-1] == noc-1: return d_result
    return g_result
# end


if __name__ == "__main__":
    P = [5, 6, 1, 3, 2, 4, 3, 5]
    g = 8
    d = 10
    # [1, 4]
    print(prom(P, g, d))