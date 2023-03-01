def rad_count(A):
    n = len(A)
    C = [0 for _ in range(n)]
    for x in A:
        C[x % n] += 1

    for i in range(n - 1):
        C[i + 1] += C[i]

    B = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        j = A[i] % n
        B[C[j] - 1] = A[i]
        C[j] -= 1

    C = [0 for _ in range(n)]
    for x in B:
        C[x // n] += 1

    for i in range(n - 1):
        C[i + 1] += C[i]

    for i in range(n - 1, -1, -1):
        j = B[i] // n
        A[C[j] - 1] = B[i]
        C[j] -= 1

    return A
# end


t = [12, 14, 5, 11]
print(t)
rad_count(t)
print(t)