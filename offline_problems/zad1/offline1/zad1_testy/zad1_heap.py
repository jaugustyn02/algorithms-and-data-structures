from zad1testy import Node, runtests


def len_of_llist(p):
    count = 0
    while p:
        p = p.next
        count += 1
    return count
# end


def heapify(i, n, tab):
     l = 2*i+1  # left(i)
     r = 2*i+2  # right(i)
     max_ind = i
     if l < n and tab[l] < tab[max_ind]:
         max_ind = l
     if r < n and tab[r] < tab[max_ind]:
         max_ind = r
     if max_ind != i:
         tab[i], tab[max_ind] = tab[max_ind], tab[i]
         heapify(max_ind, n, tab)
 # end


def heapify2(i, n, tab):
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        max_ind = i
        if l < n and tab[l] < tab[max_ind]:
            max_ind = l
        if r < n and tab[r] < tab[max_ind]:
            max_ind = r
        if max_ind == i:
            break
        tab[i], tab[max_ind] = tab[max_ind], tab[i]
        i = max_ind
        # heapify(max_ind, n, tab)
# end


def build_heap(n, tab):
    for i in range((n-1)//2, -1, -1):
        heapify(i, n, tab)
# end


def SortH(p, k):
    if k == 0:
        return p
    elif k == 1:
        head = p
        while p.next is not None:
            if p.val > p.next.val:
                p.val, p.next.val = p.next.val, p.val
                p = p.next
                if p.next is None:
                    return p
            p = p.next
        return head
    else:
        head = p
        # tworzenie tablicy o k+1 elementach potrzebnej do reprezentacji kopca
        n = len_of_llist(head)
        if k > n-1:
            k = n-1
        tab = [0 for _ in range(k+1)]
        for i in range(k+1):
            tab[i] = p.val
            p = p.next

        # tworzonenie kopca o k+1 pierwszych el. od lewej z listy, korzystając z reguły (wartość rodzica <= od wartości dzieci)
        build_heap(k + 1, tab)

        # sortowanie polega na zabieraniu z korzenia kopca el. minimalnego i umieszczaniu go w liscie od lewej strony na kolejnych pozycjach
        # a na jego miejscu umieszczaniu kolejnego od lewej elementu z listy, który nie był jeszcze w kopcu
        p, q = head, p
        for _ in range(n-k-1):
            tab[0], p.val = q.val, tab[0]
            heapify(0, k+1, tab)
            p, q = p.next, q.next

        # ostatnie k elementów umieszcza się w liście w sposób analogiczny do sortowania heap sort
        for i in range(k, 0, -1):
            tab[0], p.val = tab[i], tab[0]
            heapify(0, i, tab)
            p = p.next
        p.val = tab[0]
    return head
# end

runtests( SortH )
