from zad2testy import runtests


def partition_k(arr, low, high, k):
    i = (low - 1)
    pivot = arr[high][k]

    for j in range(low, high):
        if arr[j][k] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort_k(arr, low, high, k):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition_k(arr, low, high, k)
        quickSort_k(arr, low, pi - 1, k)
        quickSort_k(arr, pi + 1, high, k)


###############################################


def merge(l, m, r, tab):
    il = 0
    ir = 0
    l_tab = tab[l:m + 1]
    r_tab = tab[m + 1:r + 1]
    nl = m - l + 1
    nr = r - m
    for i in range(l, r + 1):
        if ir >= nr or il < nl and (
                l_tab[il][0] < r_tab[ir][0] or l_tab[il][0] == r_tab[ir][0] and l_tab[il][1] > r_tab[ir][1]):
            tab[i] = l_tab[il]
            il += 1
        else:
            tab[i] = r_tab[ir]
            ir += 1
# end


def merge_sort(l, r, tab):
    if l != r:
        m = (l + r) // 2
        merge_sort(l, m, tab)
        merge_sort(m + 1, r, tab)
        merge(l, m, r, tab)


# end


def merge_sort_right(l, r, tab):
    if l != r:
        m = (l + r) // 2
        merge_sort_right(l, m, tab)
        merge_sort_right(m + 1, r, tab)
        merge_right(l, m, r, tab)
# end


def merge_right(l, m, r, tab):
    il = 0
    ir = 0
    l_tab = tab[l:m + 1]
    r_tab = tab[m + 1:r + 1]
    nl = m - l + 1
    nr = r - m
    for i in range(l, r + 1):
        if ir >= nr or il < nl and l_tab[il][1] < r_tab[ir][1]:
            tab[i] = l_tab[il]
            il += 1
        else:
            tab[i] = r_tab[ir]
            ir += 1
# end


def depth(L):
    n = len(L)
    L.sort(key=lambda x: x[1])
    # quickSort_k(L, 0, n - 1, 1)
    # merge_sort_right(0, n-1, L)

    curr_max = L[0][1]
    curr_ind = 0
    R = [0]
    for i in range(n):
        if L[i][1] > curr_max:
            # R.append(R[curr_ind])
            R.append(0)
            curr_max = L[i][1]
            curr_ind += 1
        L[i][1] = curr_ind
        R[curr_ind] += 1

    print(R)
    merge_sort(0, n - 1, L)
    # quickSort_k(L, 0, n - 1, 0)

    max_right = -1
    max_intervals = 0
    for i in range(n - 1):
        r = L[i][1]
        if r > max_right:
            max_intervals = max(max_intervals, R[r] - 1 - i)
            max_right = r

    return max_intervals
# end


runtests(depth)
