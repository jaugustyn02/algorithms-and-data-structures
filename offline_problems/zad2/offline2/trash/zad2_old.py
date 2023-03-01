from zad2testy import runtests


def find_ind(x, l, r, L):
    if l == r:
        return l
    m = (l+r)//2
    if x < L[m][0]:
        return find_ind(x, l, m, L)
    else:
        return find_ind(x, m+1, r, L)


def find_ind2(x, l, r, L):
    while l != r:
        m = (l+r)//2
        if x < L[m][0]:
            r = m
        else:
            l = m+1
    return l


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j][0] < pivot[0] or arr[j][0] == pivot[0] and arr[j][1] > pivot[1]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


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


def depth(L):
    # max_val = 0
    #
    # for x in L:
    #     max_val = max(max_val, x[1])
    #
    # if max_val <= 10**7:
    #     n = len(L)
    #     merge_sort(0, n - 1, L)
    #     T = [0 for _ in range(max_val)]
    #
    #     for x in L:
    #         T[x[1]-1] += 1
    #     for i in range(max_val-1):
    #         T[i+1] += T[i]
    #
    #     if n < 100:
    #         print(set(T))
    #         print(T)
    #
    #     max_right = 0
    #     max_intervals = 0
    #     for i in range(n-1):
    #         r = L[i][1]
    #         if r > max_right:
    #             max_intervals = max(max_intervals, T[r-1]-1-i)
    #             max_right = r
    #
    #     return max_intervals
    #
    # else: return "siemson"

    n = len(L)
    # merge_sort(0, n-1, L)
    quickSort(L, 0, n-1)
    tab = [1 for _ in range(n)]
    max_count = 0
    n -= 1

    max_range = n - 1
    i = 0
    while i < max_range:
        imc = i + max_count + 1
        if tab[i] != 0 and L[imc][0] < L[i][1]:
            count = 0
            lim = find_ind2(L[i][1], imc, n, L)
            # if lim - i - 1 > max_count:
            for j in range(i+1, lim+1):
                if L[j][1] <= L[i][1]:
                    tab[j] = 0
                    count += 1
            if count > max_count:
                max_count = count
                max_range = n - max_count
        i += 1

    # for i in range(n):
    #     if tab[i] != 0:
    #         count = 0
    #         lim = find_ind2(L[i][1], i+1, n, L)
    #         if lim - i - 1 > max_count:
    #             for j in range(i+1, lim+1):
    #                 if L[j][1] <= L[i][1]:
    #                     tab[j] = 0
    #                     count += 1
    #             max_count = max(max_count, count)

    return max_count


runtests(depth)


# end

    # end = time()
    # print("znaleziono wynik w:", round(end - begin, 2))

    # lim = 0
    # for i in range(n-1):
    #     if I[i]:
    #         count = 0
    #         right = L[i][1]
    #         lim = binary_search(right+1, lim+1, n, L)
    #         if lim - i - 1 > max_count:
    #             for j in range(i+1, lim):
    #                 if L[j][1] <= right:
    #                     I[j] = 0
    #                     count += 1
    #             max_count = max(max_count, count)

    # return max_count
