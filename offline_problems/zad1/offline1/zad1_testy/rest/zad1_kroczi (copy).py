from zad1testy import Node, runtests


def SortH(p, k):
    first = p
    s = p
    d = 1
    while s.next != None:
        s = s.next
        d += 1
    def przepiecia(a, b):
        nonlocal first
        if a > b:
            b, a = a, b
        if a == 0:
            qa = first
            if b == 1:
                qb = qa.next
                qa.next, qb.next = qb.next, qa
                first = qb
            else:
                qb = qa
                for  in range(b-1):
                    qb = qb.next
                prevb = qb
                qb = qb.next
                qb.next, prevb.next, qa.next = qa.next, qa, qb.next
                first = qb
        else:
            qa = first
            for  in range(a-1):
                qa = qa.next
            if b == a+1:
                prewa = qa
                qa = qa.next
                qb = qa.next
                prewa.next, qb.next, qa.next = qb, qa, qb.next
            else:
                prewa = qa
                qa = qa.next
                prewb = prewa
                for  in range(b-a):
                    prewb = prewb.next
                qb = prewb.next
                prewa.next, qb.next, prewb.next, qa.next = qb, qa.next, qa, qb.next

    def wart(a):
        nonlocal first
        z = first
        for  in range(a):
            z = z.next
        return z.val
    def heapify(n, i):
        max_ind = i
        l = 2i+1
        r = 2i+2
        if l < n and wart(l) > wart(max_ind):
            max_ind = l
        if r < n and wart(r) > wart(max_ind):
            max_ind = r
        if max_ind != i:
            przepiecia(i, max_ind)
            heapify(n, max_ind)
    def heap_sort():
        nonlocal d
        n = d
        for i in range(n, -1, -1):
            heapify(n, i)
        for i in range(n-1, 0, -1):
            przepiecia(0, i)
            heapify(i, 0)
	heap_sort()

	return first


runtests( SortH )
