# Zadanie 2. (problem sumy podzbioru)


def subset(A, T):
    n = len(A)
    F = [[0 for _ in range(T+1)] for _ in range(n+1)]
    for i in range(n+1):
        F[i][0] = 1
    for i in range(n+1):
        for t in range(T+1):
            F[i][t] = F[i-1][t]
            if t - A[i-1] >= 0:
                F[i][t] = F[i-1][t-A[i-1]]
    return F[n][T]


A = [1, 2, 3, 5, 6, 19]
T = 18
print(subset(A, T))

# def subseq_sum(i, curr_sum, n, S, A):
#     if curr_sum == S:
#         return True
#     if curr_sum > S or i == n:
#         return False
#     return (subseq_sum(i+1, curr_sum+A[i], n, S, A) or
#             subseq_sum(i+1, curr_sum, n, S, A))
# # end
#
#
# def subseq_sum_nlogn(S, A):
#     A.sort()
#     print(A)
#     n = len(A)
#     i = 0
#     j = 0
#     curr_sum = 0
#     while curr_sum != S:
#         if curr_sum < S:
#             if j < n:
#                 curr_sum += A[j]
#                 j += 1
#             else:
#                 return False
#         elif i < n:
#             curr_sum -= A[i]
#             i += 1
#         else:
#             return False
#     if curr_sum == S:
#         return True
#     return False
# # end


# A = [2, 5, 2, 6, 7, 10, 2, 4, 9]
# B = [0, 2, 4]
# S = 12
# print(subseq_sum(0, 0, len(A), S, A))
# print(subseq_sum_nlogn(S, A))
# print(subseq_sum_nlogn(1, B))
