from random_list import create_random_list
from random import randint


def knapsack01(W, wt, val):
    T = [[0 for _ in range(W+1)] for _ in range(len(wt)+1)]
    for i in range(1, len(wt)+1):
        for j in range(1, W+1):
            if j < wt[i-1]:
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = max(T[i-1][j], val[i-1] + T[i-1][j-wt[i-1]])
    return T[len(wt)][W]
# end


def knapsack01_fit(W, wt, val):
    T = [0 for _ in range(W+1)]
    for i in range(len(wt)):
        for j in range(W, wt[i]-1, -1):
            # print(j, wt[i])
            T[j] = max(T[j], val[i] + T[j-wt[i]])
    return T[W]
# end


def knapsack01_sort(W, wt, val):
    indices = [i for i in range(len(wt))]
    indices.sort(key=lambda i:wt[i])
    T = [0 for _ in range(W+1)]
    for i in indices:
        for j in range(W, wt[i]-1, -1):
            # print(j, wt[i])
            T[j] = max(T[j], val[i] + T[j-wt[i]])
    return T[W]
# end


# val = [60, 100, 120, 221]
# wt = [10, 20, 30, 50]
# val = [5, 3, 3]
# wt = [4, 3, 3]
# W = 6
# print(knapsack_01(W, wt, val))

# print("   ", end="")
# for i in range(len(ls[0])):
#     print(i, end="  ")
# print()
# for i in range(len(ls)):
#     print(i, end=" ")
#     print(ls[i])
#
# print()

# N = 1000
# a = 1
# b = 10000
# wt = create_random_list(N, a, b)
# val = create_random_list(N, a, b)
# W = randint(a+50, b)
# print(W)

W = 1
wt = [1, 1]
val = [2, 1]

print(knapsack01_fit(W, wt, val))
print(knapsack01_sort(W, wt, val))
print(knapsack01(W, wt, val))

# for i in range(len(ls)):
#     print(i, end="\t")
# print()
# for i in range(len(ls)):
#     print(ls[i], end="\t")
