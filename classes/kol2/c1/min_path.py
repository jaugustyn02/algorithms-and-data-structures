# zad. 7 (wędrówka po szachownicy)


def min_path_2(A):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        F[0][i] = A[0][i] + F[0][i - 1]
        F[i][0] = A[i][0] + F[i - 1][0]
    for i in range(1, n):
        for j in range(1, n):
            F[i][j] = A[i][j] + min(F[i - 1][j], F[i][j - 1])

    return F[n - 1][n - 1]
# end


def min_path(board):
    n = len(board)
    for i in range(2, n):
        board[0][i] += board[0][i-1]
        board[i][0] += board[i-1][0]
    for i in range(1, n):
        for j in range(1, n):
            board[i][j] += min(board[i-1][j], board[i][j-1])

    return board[n-1][n-1]
# end


def find_min_path(board):
    n = len(board)
    for i in range(2, n):
        board[0][i] += board[0][i - 1]
        board[i][0] += board[i - 1][0]
    for i in range(1, n):
        for j in range(1, n):
            board[i][j] += min(board[i - 1][j], board[i][j - 1])

    path = [0 for _ in range(2 * n - 1)]
    path[-1] = (n, n)
    i, j = n-1, n-1
    while i > 0 or j > 0:
        if j == 0 or (i > 0 and board[i-1][j] < board[i][j-1]):
            path[i+j-1] = (i, j+1)
            i -= 1
        else:
            path[i+j-1] = (i+1, j)
            j -= 1

    return board[n - 1][n - 1], path
# end


B = [
    [0, 2, 8, 6, 8],
    [3, 6, 2, 5, 12],
    [9, 5, 1, 20, 10],
    [10, 3, 15, 16, 6],
    [2, 7, 9, 12, 0]
]

B_cp = [[el for el in row] for row in B]

print(min_path(B))
# print(find_min_path(B_cp))
print(min_path_2(B_cp))
