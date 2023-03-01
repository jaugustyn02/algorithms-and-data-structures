# Jan Augustyn
# Dla k < 200: Algorytm wykorzystuje kopiec (w. rodzica <= w.dzieci, najm. el. w korzeniu),
# do przetrzymywania k+1 elementów. El. w korzeniu umieszczany jest po koleji od lewej w l. liscie,
# a na jego miejscu umieszczany jest następny od lewej el. który nie był jeszcze w kopcu.
# Dla k >= 200: Najpierw, posortowane zostaje 2k el. metodą Merge Sort (pierwsze k el. na odpowiednich pozycjach).
# Następnie powtarzane jest: 1) sortowanie kolejnych k el. (merge sort) 2) scalanie 2 list o długości k.
# Dla k = 1, l. lista sortowana analogicznie do Bubble Sort. Znacząco mniejszy czas wykonywania dla dużych n.
# Złożoność czasowa: O(nlog(k))
# Złożoność czasowa względem k:
# dla k=O(1) wynosi O(n)
# dla k=O(log(n)) wynosi O(nlog(log(n)))
# dla k=O(n) wynosi O(nlog(n))
# Złożoność pamięciowa:
# Dla k = 1 i k >= 200: w miejscu
# Dla 1 < k < 200: O(k)

from zad1testy import Node, runtests


def len_of_llist(p):
    count = 0
    while p:
        p = p.next
        count += 1
    return count
# end


def heapify(i, n, tab):
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
# end


def build_heap(n, tab):
    for i in range((n - 1) // 2, -1, -1):
        # heapify(i, n, tab)
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
# end


def k_heap_sort(p, k):
    head = p
    n = len_of_llist(head)
    if k > n - 1:
        k = n - 1

    tab = [0 for _ in range(k + 1)]
    for i in range(k + 1):
        tab[i] = p.val
        p = p.next

    build_heap(k + 1, tab)

    p, q = head, p
    for _ in range(n - k - 1):
        tab[0], p.val = q.val, tab[0]
        # heapify(0, k+1, tab)
        i = 0
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            max_ind = i
            if l <= k and tab[l] < tab[max_ind]:
                max_ind = l
            if r <= k and tab[r] < tab[max_ind]:
                max_ind = r
            if max_ind == i:
                break
            tab[i], tab[max_ind] = tab[max_ind], tab[i]
            i = max_ind

        p, q = p.next, q.next

    for i in range(k, 0, -1):
        tab[0], p.val = tab[i], tab[0]
        # heapify(0, i, tab)
        j = 0
        while True:
            l = 2 * j + 1
            r = 2 * j + 2
            max_ind = j
            if l < i and tab[l] < tab[max_ind]:
                max_ind = l
            if r < i and tab[r] < tab[max_ind]:
                max_ind = r
            if max_ind == j:
                break
            tab[j], tab[max_ind] = tab[max_ind], tab[j]
            j = max_ind

        p = p.next
    p.val = tab[0]
    return head
# end


def merge(head1, head2):
    sentinel = Node()
    tmp = sentinel

    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            tmp.next = head1
            head1 = head1.next
        else:
            tmp.next = head2
            head2 = head2.next
        tmp = tmp.next

    while head1 is not None:
        tmp.next = head1
        head1 = head1.next
        tmp = tmp.next

    while head2 is not None:
        tmp.next = head2
        head2 = head2.next
        tmp = tmp.next

    return sentinel.next, tmp
# end


def find_mid(head):
    p = head
    q = head.next
    while q is not None and q.next is not None:
        p = p.next
        q = q.next.next
    return p
# end


def merge_sort(head1):
    if head1.next is None:
        return head1, head1

    mid = find_mid(head1)
    head2 = mid.next
    mid.next = None

    new_head1, _ = merge_sort(head1)
    new_head2, _ = merge_sort(head2)
    return merge(new_head1, new_head2)
# end


def find_k(p, k):
    i = 0
    while p.next is not None and i < k:
        p = p.next
        i += 1
    return p
# end


def k_merge_sort(p, k):
    tail2 = find_k(p, 2 * k - 1)
    head2 = tail2.next
    tail3 = find_k(tail2, k)
    head3 = tail3.next

    tail2.next = None
    main_head, tail2 = merge_sort(p)

    tail1 = find_k(main_head, k - 1)
    while head3 is not None:
        tail3.next = None
        head2, tail3 = merge_sort(head2)

        tail1.next, tail3 = merge(tail1.next, head2)

        tail1, head2, tail3 = find_k(tail1, k), head3, find_k(head3, k - 1)
        head3 = tail3.next

    if head2 is not None:
        head2, _ = merge_sort(head2)
        tail1.next, _ = merge(tail1.next, head2)
    return main_head
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
    elif k < 200:
        return k_heap_sort(p, k)
    else:
        return k_merge_sort(p, k)
# end


runtests(SortH)
