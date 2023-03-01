# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations

V = 4


# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path


def d(i, j, arr):
    x1, y1 = arr[i]
    x2, y2 = arr[j]
    a = x2 - x1
    b = y2 - y1
    return (a**2 + b**2)**0.5
# end


# Driver Code
if __name__ == "__main__":
    # matrix representation of graph
    # graph = [[0, 10, 15, 20], [10, 0, 35, 25],
    #          [15, 35, 0, 30], [20, 25, 30, 0]]

    cords = [(1, 2), (5, 2), (6, 8), (2, 2), (13, 5), (6, 9)]
    graph = [[d(i, j, cords) for j in range(len(cords))] for i in range(len(cords))]
    print(graph)
    s = 0
    print(travellingSalesmanProblem(graph, s))
