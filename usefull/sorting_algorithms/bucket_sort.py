def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        j = i - 1
        curr = A[i]
        while j >= 0 and curr < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = curr
# end


def interval_bucket_sort(T, a, b):
    n = len(T)
    buckets_range = b - a
    bucket_size = buckets_range / n
    buckets_num = int(buckets_range // bucket_size) + 1
    # print(buckets_range, bucket_size, buckets_num)

    buckets = [[] for _ in range(buckets_num)]

    for i in range(n):
        # print(T[i], "/", bucket_size, "=", T[i]//bucket_size)
        buckets[int(T[i] // bucket_size)].append(T[i])

    for i in range(buckets_num):
        insertion_sort(buckets[i])
        # print("[", round(i*bucket_size, 2), "-", round((i+1)*bucket_size, 2), ") ", buckets[i], sep="")

    k = 0
    for i in range(buckets_num):
        for j in range(len(buckets[i])):
            T[k] = buckets[i][j]
            k += 1
# end


t = [0.25, 3.75, 6.0, 3.3, 4.5, 5.6, 8.4, 7.12, 9.42, 1.23, 2.66, 9.13, 4.65, 1.50, 10.0, 11.0, 10.14, 7.15]
print(t)
bucket_sort(t, 0, 11)
print(t)
