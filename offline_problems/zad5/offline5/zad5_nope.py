from zad5testy import runtests


def plan(T):
    n = len(T)
    F = [[n for _ in range(n-i)] for i in range(n)]
    M = [n for _ in range(n)]
    F[0][min(T[0], n - 1)] = 0
    M[min(T[0], n - 1)] = 0
    N = n
    fuel_used = None
    for i in range(1, n):
        N -= 1
        # c = min(T[i], n-i-1)
        if T[i] > 0 or i == n-1:
            for j in range(N-1, -1, -1):  # n-i-c-1
                c = min(T[i], N-1-j)
                no_steps = M[i+j] + 1
                # if i in (0, 5, 7, 15):
                #     print(i, j, c, j + c, M[i + j])
                if no_steps < F[i][j+c]:
                    F[i][j+c] = no_steps
                    if no_steps < M[i+j+c]:
                        M[i+j+c] = no_steps
                        # if c < T[i]:
                        if i+j+c == n-1:
                            fuel_used = c
                            min_steps = no_steps

                # F[i][j+c] = min(M[i+j]+1, F[i][j+c])
                # M[i+j+c] = min(M[i+j+c], F[i][j+c])

    # for i in range(len(F)):
    #     print(i, "({})".format(T[i]), F[i])
    # print(M)

    result = []
    i = n-2
    j = 1
    steps = F[n-1][0]-1
    while i >= 0:
        # print(i, j, steps)
        while i > 0 and j < n-i and F[i][j] != steps:
            i -= 1
            j += 1
        result.append(i)
        if fuel_used is not None and min_steps == F[i][j]:
            # print("Tutaj:", i, j, fuel_used, j - fuel_used + 1)
            j = j - fuel_used + 1
            fuel_used = None
        else:
            j = j - T[i] + 1
        i -= 1
        steps -= 1

    return list(reversed(result))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )