# Zadanie 3. (najdłuższy wspólny podciąg)

#     A B C C D
#     0 0 0 0 0
# D 0 0 0 0 0 1
# C 0 0 0 1 1 1
# A 0 1 1 1 1 1
# B 0 1 2 2 2 2
# D 0 1 2 2 2 3

def length(A, B):
    n = len(A)
    F = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])

    return F[n][n]
# end



def longest_common_subseq(A, B):
    na = len(A)
    nb = len(B)
    LCS = [[0 for _ in range(nb+1)] for _ in range(na+1)]
    for i in range(1, na+1):
        for j in range(1, nb+1):
            if A[i-1] == B[j-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

    return LCS[na][nb]
# end


def longest_common_subseq_fit(A, B):
    na = len(A)
    nb = len(B)
    LCS = [0 for _ in range(nb+1)]
    for i in range(1, na+1):
        prev = LCS[0]
        for j in range(1, nb+1):
            if A[i-1] == B[j-1]:
                LCS[j], prev = prev + 1, LCS[j]
            else:
                LCS[j], prev = max(LCS[j], LCS[j-1]), LCS[j]

    return LCS[nb]
# end


# A = [2, 3, 1, 4, 0, 7, 2, 3, 4]
# B = [4, 3, 9, 9, 5, 9, 9, 3, 2]
# B = [2, 7, 3, 3, 4, 9, 2, 3, 0]  # 2 3 4 2 3
A = "AGGTAB"
B = "GXTXAYB"
print(longest_common_subseq(A, B))
print(longest_common_subseq_fit(A, B))