# Jan Augustyn
# Algorytm częściowo opiera się na sortowaniu Heap Sort. Najpierw tworzy kopiec o k+1 elementach
# (w. rodzica <= w.dzieci, najm. el. w korzeniu). Następnie el. w korzeniu umieszczany jest po koleji od lewej
# w linked liście, a na jego miejscu umieszcza się kolejny el. z listy, który jeszcze nie był w kopcu.
# Ostatnie k elementów umieszcza się w wynikowej liście analogicznie do algorytmu Heap Sort.
# Wyjątek dla k=1, lista sortowana analogicznie do Bubble Sort w 1 przejściu, bez tworzenia dodatkowych struktur, co ma na celu zmniejszenie czasu wykonywania się dla dużych n.
# Oczekiwana złożoność O(nlog(k))
# Złożoność czasowa względem k:
# dla k=O(1) wynosi O(n)
# dla k=O(logn) wynosi O(n)
# dla k=O(n) wynosi O(nlog(n))
# Złożoność pamięciowa wynosi O(k)

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
    for i in range((n-1)//2, -1, -1):
        heapify(i, n, tab)
# end


def SortH(p,k):
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
 
        n = len_of_llist(head)
        if k > n-1:
            k = n-1
        tab = [0 for _ in range(k+1)]
        for i in range(k+1):
            tab[i] = p.val
            p = p.next

        build_heap(k + 1, tab)

        p, q = head, p
        for _ in range(n-k-1):
            tab[0], p.val = q.val, tab[0]
            heapify(0, k+1, tab)
            p, q = p.next, q.next

        for i in range(k, 0, -1):
            tab[0], p.val = tab[i], tab[0]
            heapify(0, i, tab)
            p = p.next
        p.val = tab[0]
    return head
# end


runtests( SortH ) 
