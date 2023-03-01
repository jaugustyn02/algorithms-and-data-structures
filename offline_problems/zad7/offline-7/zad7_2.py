from zad7testy import runtests


def droga( G ):
    N = len(G)
    visited = [0 for _ in range(N)]
    indices = [[0, 0] for _ in range(N)]
    prev = None
    for first_gate in range(2):
        stack = [[0, first_gate]]
        visited[0] = 1
        while len(stack) > 0:
            v, exit_gate = stack[-1]
            if exit_gate is None:
                if prev in G[v][0]: exit_gate = 1
                else: exit_gate = 0
                stack[-1][1] = exit_gate

            if len(stack) == len(G) and 0 in G[v][exit_gate] and v in G[0][(stack[0][1]+1) % 2]:
                return [v[0] for v in stack]

            i = indices[v][exit_gate]
            n = len(G[v][exit_gate])
            while i < n and visited[G[v][exit_gate][i]] == 1:
                i += 1

            if i == n:
                visited[v] = 0
                indices[v] = [0, 0]
                stack.pop()
            else:
                indices[v][exit_gate] = i + 1
                prev = v
                u = G[v][exit_gate][i]
                visited[u] = 1
                stack.append([u, None])
    return None
# end


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )