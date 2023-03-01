def black_forest(T):
    n = len(T)
    F = [0 for _ in range(n)]
    F[0] = T[0]
    F[1] = max(T[0], T[1])
    for i in range(2, n):
        F[i] = max(F[i-1], F[i-2] + T[i])

    result = []
    i = n-2
    while i > -1:
        if F[i+1] > F[i]:
            result.append(i+1)
            i -= 2
        else:
            result.append(i)
            i -= 3
    if result[-1] == 2:
        result.append(1)
    print(F[-1])
    return list(reversed(result))
# end


# T = [1, 3, 2, 1, 1, 1, 1, 1]
# F = [1, 3, 3, 4, 4, 5, 5, 6]
# F = [1, 1, 3, 3 ...]

# T = [1, 2, 2, 2, 1]
T = [5, 3, 1, 3, 7, 6, 1]
print(black_forest(T))
