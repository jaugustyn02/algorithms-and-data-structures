from zad7testy import runtests


def droga( G ):
    def f(i, prev, n, last_gate=None):
        nonlocal result, visited, G
        for gate in range(2):
            if prev in G[i][(gate+1) % 2]:
                if i == 0: last_gate = (gate+1) % 2
                if n == len(G) and 0 in G[i][gate] and i in G[0][last_gate]:
                    result.append(i)
                    return 1
                visited[i] = 1
                for v in G[i][gate]:
                    if visited[v] == 0 and f(v, i, n + 1, last_gate):
                        result.append(i)
                        return 1
                visited[i] = 0
        return 0
    # end

    result = []
    n = len(G)
    visited = [0 for _ in range(n)]
    if n > 0 and len(G[0][1]) > 0 and not f(0, G[0][1][0], 1) and len(G[0][0]) > 0:
        f(0, G[0][0][0], 1)
    if len(result) == 0: return None
    return result
# end


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )