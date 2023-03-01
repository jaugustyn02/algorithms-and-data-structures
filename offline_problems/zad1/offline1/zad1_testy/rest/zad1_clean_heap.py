from zad1testy import Node, runtests


def create_llist(elements):
    head = Node()
    head.val = elements[0]
    prev = head
    for i in range(1, len(elements)):
        new = Node()
        new.val = elements[i]
        prev.next = new
        prev = new
    return head


# end


def print_llist(head):
    tmp = head
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print()
# end


# new_head = create_llist((3, 2, 1, 6, 5, 4, 10, 7))
# print_llist(new_head)

# KONIEC CZĘŚCI POMOCNEJ


def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2


def len_of_llist(p):
    count = 0
    while p:
        p = p.next
        count += 1
    return count
# end


def heapify(i, n, tab):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and tab[l] > tab[max_ind]:
        max_ind = l
    if r < n and tab[r] > tab[max_ind]:
        max_ind = r
    if max_ind != i:
        tab[i], tab[max_ind] = tab[max_ind], tab[i]
        heapify(max_ind, n, tab)
# end


def build_heap(n, tab):
    for i in range(parent(n-1), -1, -1):
        heapify(i, n, tab)
# end


def SortH(p, k):
    head = p
    # tworzenie tablicy reprezentującej podaną linked list'e
    n = len_of_llist(head)
    tab = [0 for _ in range(n)]
    for i in range(n):
        tab[i] = p.val
        p = p.next
    # print(tab)

    # sortowanie tablicy metodą heap sort
    build_heap(n, tab)
    # print(tab)
    for i in range(n-1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(0, i, tab)
    # print(tab)

    # przypisanie posortowanych wartości do węzłów linked listy
    p = head
    for i in range(n):
        p.val = tab[i]
        p = p.next

    return head
# end


# new_head = SortH(new_head, 2)
# print_llist(new_head)
runtests( SortH )
