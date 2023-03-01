from random_list import create_dense_list, create_random_list


def no_tail_qsort(p, r, arr):
    while p < r:
        q = std_partition(p, r, arr)
        if q - p > r - q:
            no_tail_qsort(p, q - 1, arr)
            p = q + 1
        else:
            no_tail_qsort(q + 1, r, arr)
            r = q - 1
# end


def std_partition(p, r, arr):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def std_qsort(p, r, arr):
    if p < r:
        q = std_partition(p, r, arr)
        std_qsort(p, q-1, arr)
        std_qsort(q+1, r, arr)
# end


if __name__ == "__main__":
    # new_ls = create_dense_list(1000, 1, 1000, 100)
    new_ls = create_random_list(10**5, 1, 10**24)
    cp_ls = new_ls
    # std_qsort(0, len(new_ls)-1, new_ls)
    no_tail_qsort(0, len(new_ls)-1, new_ls)
    if new_ls == sorted(cp_ls):
        print("siem")
    else:
        print("nie siem")