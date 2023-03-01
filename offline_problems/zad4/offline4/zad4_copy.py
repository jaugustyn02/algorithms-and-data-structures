from zad4testy import runtests


def select_buildings(T, p):
    p += 1  # bo kurwa nie wiem czy budżet może być równy p czy nie

    def cmp(i):
        nonlocal T
        return T[i][1]
    # end

    def cmp2(i):
        nonlocal T
        return T[i][2]
    # end

    N = len(T)
    indices = [i for i in range(N)]
    indices.sort(key=cmp2)
    indices.sort(key=cmp)
    # print(indices)

    F = [[(0, 0) for _ in range(p)]
         for _ in range(N+1)]

    # dorm = [height, beginning, end, cost]
    for i in range(1, N+1):
        dorm = T[indices[i-1]]
        for j in range(1, p):
            if dorm[3] > j:
                F[i][j] = F[i-1][j]
            else:
                max_poss_val = 0
                cost = dorm[3]
                beg = dorm[1]
                for k in range(i-1, 0, -1):
                    if F[k][j-cost][1] < beg:
                        max_poss_val = F[k][j-cost][0]
                        break

                total_value = dorm[0] * (dorm[2]-dorm[1]) + max_poss_val
                if F[i-1][j][0] > total_value:
                    F[i][j] = F[i-1][j]
                elif F[i-1][j][0] == total_value:
                    F[i][j] = (total_value, min(F[i-1][j][1], dorm[2]))
                else:
                    F[i][j] = (total_value, dorm[2])

    result = []
    i = N
    j = p-1
    max_value = F[i][j][0]
    while max_value > 0:
        while i > 0 and F[i][j] == F[i-1][j]:
            i -= 1
        # print("wybieram:", indices[i-1], T[indices[i-1]])
        result.append(indices[i-1])
        dorm = T[indices[i - 1]]
        max_value -= dorm[0] * (dorm[2] - dorm[1])
        end = dorm[1]
        # print(j, T[indices[i - 1]][3], j-T[indices[i-1]][3])
        j -= T[indices[i-1]][3]
        i -= 1
        while i > 0 and end <= F[i][j][1]:
            i -= 1

    # if N < 12:
    #     for i in range(N):
    #         print(i, ")", indices[i], T[indices[i]])
    #     # for i, row in enumerate(F):
    #     #     print(i, row)
    # print(F[-1][-1][0])

    return sorted(result)

    # f = open(str(F[-1][-1][0]) + "-output.txt", "w")
    #
    # for i in range(N):
    #     dorm = T[indices[i]]
    #     f.write(str(dorm[0] * (dorm[2] - dorm[1])) + " " + str(indices[i]) + " " + str(T[indices[i]]) + "\n")
    #     # f.write("[" + str(dorm[0] * (dorm[2] - dorm[1])) + ", " + str(dorm[1]) + ", " + str(dorm[2]) + "], ")
    # f.write("\n")
    #
    # for row in F:
    #     for x in row:
    #         f.write(str(x))
    #         f.write("\t")
    #     f.write("\n")
    # f.close()
    # # print(F[-1][-1])
    return sorted(result)
# end


# runtests( select_buildings )


T = [
    [3, 1, 3, 2],
    [4, 1, 3, 1],
    [3, 4, 5, 2]
]

p = 4

print(select_buildings(T, p))
