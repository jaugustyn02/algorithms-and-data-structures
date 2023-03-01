def counting_sort(A, n, k):
    C = [0 for _ in range(k)]

    for x in A:
        C[x] += 1

    for i in range(k-1):
        C[i+1] += C[i]

    B = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    A[:] = B[:]
# end


t = [1, 5, 8, 11, 12, 3, 9, 4, 4, 2]
print(t)
counting_sort(t, len(t), max(t)+1)
print(t)