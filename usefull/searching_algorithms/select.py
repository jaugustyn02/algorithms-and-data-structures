def partition(p, r, arr):
    pivo = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] < pivo:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[r], arr[i+1] = arr[i+1], arr[r]
    return i + 1
# end


def select(p, r, k, arr):
    if p == r: return arr[p]
    q = partition(p, r, arr)
    if q == k: return arr[q]
    if q > k:
        return select(p, q - 1, k, arr)
    return select(q + 1, r, k, arr)
# end


T = [2, 432, 22, 6, 23, 2, 767, 32, 12]
print(T)
print(select(0, len(T) - 1, 3, T))
print(select(3+1, len(T) - 1, 5, T))
print(T)
print(sorted(T))
